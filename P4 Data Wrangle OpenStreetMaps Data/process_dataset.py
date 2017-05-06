import os
import collections
import pprint
import xml.etree.cElementTree as ET
import re
import codecs
import csv
import copy
import json

OSM_FILE = "san-jose_california.osm"

def get_element(osm_file, tags=('node', 'way', 'relation')):
    context = iter(ET.iterparse(osm_file, events=('start', 'end')))
    _, root = next(context)
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            yield elem
            root.clear()

street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        street_types[street_type]+=1

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")

def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = collections.defaultdict(int)
    for event, elem in ET.iterparse(osm_file):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types



expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons", "Cove", "Alley", "Park", "Way", "Walk" "Circle", "Highway", 
            "Plaza", "Path", "Center", "Mission"]

mapping = { "Ave": "Avenue",
            "Ave.": "Avenue",
            "avenue": "Avenue",
            "ave": "Avenue",
            "Blvd": "Boulevard",
            "Blvd.": "Boulevard",
            "Blvd,": "Boulevard",
            "Boulavard": "Boulevard",
            "Boulvard": "Boulevard",
            "Ct": "Court",
            "Dr": "Drive",
            "Dr.": "Drive",
            "E": "East",
            "Hwy": "Highway",
            "Ln": "Lane",
            "Ln.": "Lane",
            "Pl": "Place",
            "Plz": "Plaza",
            "Rd": "Road",
            "Rd.": "Road",
            "St": "Street",
            "St.": "Street",
            "st": "Street",
            "street": "Street",
            "square": "Square",
            "Sq": "Square",
            "parkway": "Parkway"
            }


def update_name(name, mapping, expected):
    words = name.split()
    st_type = words[-1]
    if st_type in mapping:
        return name.replace(st_type, mapping[st_type])
    elif st_type in expected:
        return name
    else: return name


for i in street_types.keys():
    audit_list = mapping.keys()
    name = update_name(i, mapping, expected)
    print ("Before updating:", i, "==>", "after updating:", name)

postcode = set()
for elem in get_element(OSM_FILE, tags = ("tag",)):
    if elem.get('k') == "addr:postcode":
        postcode.add(elem.get('v')) 
    elem.clear()




def audit_zipcode(invalid_zipcodes, zipcode):
    twoDigits = zipcode[0:2]
    
    if twoDigits != 94 or twoDigits != 95 or not twoDigits.isdigit():
        invalid_zipcodes[twoDigits].add(zipcode)
        
def is_zipcode(elem):
    return (elem.attrib['k'] == "addr:postcode")

def audit_zip(osmfile):
    osm_file = open(osmfile, "r")
    invalid_zipcodes = collections.defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_zipcode(tag):
                    audit_zipcode(invalid_zipcodes,tag.attrib['v'])

    return invalid_zipcodes

OSM_FILE.encode("utf-8")
zipcode = audit_zip(OSM_FILE)
pprint.pprint(dict(zipcode))


def update_zip(zipcode):
    zipChar = re.findall('[a-zA-Z]*', zipcode)
    if zipChar == "CU":
        return [None]
    if zipChar == "CA":
        updateZip = re.findall(r'\d+', zipcode)
        if (len(updateZip) > 0):
            return (re.findall(r'\d+', zipcode))[0]
    elif (len(re.findall(r'\d+', zipcode)) > 0):
        return (re.findall(r'\d+', zipcode))[0]


for street_type, ways in zipcode.iteritems():
    for name in ways:
        better_name = update_zip(name)
        print (name, "=>", better_name)



CREATED = [ "version", "changeset", "timestamp", "user", "uid"]

def shape_element(element):
    node = {}
    if element.tag == "node" or element.tag == "way" :
        node['id']= element.get('id')
        node['type'] = element.tag
        node['visible'] = element.get('visible')
        node['created'] ={}
        for key in CREATED:
            node['created'][key] = element.get(key)
        if element.get('lat') != None and element.get('lon') != None:
            node['pos'] = [ float(element.get('lat')), float(element.get('lon'))]
       
        address = {}
        node_refs = []
        for child in element:
            if child.tag =="tag":
                k = child.get('k')
                
                val = child.get('v')
                if k and val:
                    
                    if re.search('^addr:', k):
                       
                        key = re.findall('^addr:(.+$)', k)[0]
                        if key == "postcode":
                            val = update_zip(val)
                        elif key == "street":
                            val = update_name(val, mapping, expected)
                        else: pass
                        address[key]= val


                    else: 
                        node[k]= val
            
            elif child.tag == 'nd':
                node_refs.append(child.get('ref'))
        if address:
            node["address"] = address
        if node_refs:
            node["node_refs"] = node_refs
        return node
    else:
        return None


import time

def process_map(file_in, pretty = False):
    t0 = time.time()
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        
        for element in get_element(file_in, tags=("node", "way")):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
            
    t1 = time.time()

    total = t1-t0
    print ("total process time:", total)
    

process_map("san-jose_california.osm")