# P3: Data Wrangle OpenStreetMaps Data

## Project Overview
I went to https://mapzen.com/data/metro-extracts/metro/san-jose_california/ and downloaded OSM XML file. I used data munging techniques, such as assessing the quality of the data for validity, accuracy, completeness, consistency and uniformity, to clean the OpenStreetMap data for san jose area. Finally, I chose MongoDB as the data schema to do the analysis.

## Conclusion
During this project, I audited, cleaned and explored San Jose OpenStreetMap data. I found two problems. One is the addr:street - street name is inconsistent such as "Rd" and "Road". I created a mapping for those stree names and delete unexpected street names. The other problems is the postcode. I identified unexpected "CA" and "CU", and updated all 9 digits to 5 digits, which I think is a good for further analysis.
When I looking at tag at the very beginning of the project, I found that there are hundreds of tags there. So one of my suggestions is to reduce the amount of tags and created more general tag names. In that case, we can save time to audit and clean the dataset.

## Report
To see the complete report, please go to [Data Wrangling - OpenStreetMap.ipynb](https://github.com/Ruofei29/Udacity-Data-Analyst-Nanodegree/blob/master/P3%20Data%20Wrangle%20OpenStreetMaps%20Data/Data%20Wrangling%20-%20OpenStreetMap.ipynb)

