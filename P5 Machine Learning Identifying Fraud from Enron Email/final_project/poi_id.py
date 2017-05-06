#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")


from tester import dump_classifier_and_data
import numpy as np
import pandas as pd

with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)



df = pd.DataFrame.from_dict(data_dict, orient='index')
df = df.replace('NaN', np.nan)
# Delete "Total" row
df = df.drop(['TOTAL'])
# Fill 0 to replace NULL
df=df.fillna(0)

my_dataset = df.to_dict('index')

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.preprocessing import MinMaxScaler
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

labels_1 = df.poi
features_1 = df[['salary','bonus','total_stock_value','exercised_stock_options']]

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi','salary','bonus','total_stock_value','exercised_stock_options'] # You will need to use more features


### Load the dictionary containing the dataset

### Task 2: Remove outliers
### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.

### Extract features and labels from dataset for local testing


### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

#split train and test dataset
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features_1, labels_1, test_size = 0.3)


# Provided to give you a starting point. Try a variety of classifiers.

#train AdaBoost Model
# from sklearn.ensemble import AdaBoostClassifier
# from sklearn.grid_search import GridSearchCV

# c = AdaBoostClassifier()
# parameters = {'n_estimators': [150,160, 170,180,190,200,210,220,230],
#                'algorithm': ['SAMME', 'SAMME.R'],
#                'learning_rate': [.4,.5, .6,.7,.8,.9,1,1.1,1.2,1.3]}
# grid_search = GridSearchCV(c, parameters,scoring='recall')
# grid_search.fit(features_train, labels_train)
# clf=grid_search.best_estimator_
# print "Accuracy score:", grid_search.score(features_test,labels_test)

# from sklearn.metrics import recall_score,precision_score
# pred = grid_search.predict(features_test)
# recall = recall_score(labels_test,pred)
# precision = precision_score(labels_test,pred)

# print "\nPrecision (POIs):", precision
# print "Recall (POIs)", recall

from sklearn.naive_bayes import GaussianNB
from sklearn.grid_search import GridSearchCV

clf = GaussianNB()
parameters = {}
grid_search = GridSearchCV(clf, parameters,scoring = 'recall')
grid_search.fit(features_train, labels_train)

print "Accuracy score:", grid_search.score(features_test,labels_test)

from sklearn.metrics import recall_score,precision_score
pred = grid_search.predict(features_test)
recall = recall_score(labels_test,pred)
precision = precision_score(labels_test,pred)

print "\nPrecision (POIs):", precision
print "Recall (POIs)", recall



### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!


### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)