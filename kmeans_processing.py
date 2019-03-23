'''
Created on 2019 M03 18

@author: Anthony
'''
# from matplotlib import pyplot
# from nltk.stem.porter import *

import pickle

from sklearn import cluster
from sklearn.decomposition import PCA

import numpy as np
import pandas as pd

vectors_file = open('yeet.pkl', 'rb')

results = pickle.load(vectors_file)

vectors_file.close()

results = np.array(results)

pca = PCA(3)
pca.fit(results)
pca_data = pd.DataFrame(pca.transform(results))
print("PCA HEAD DATA")
print(pca_data.head())

kmeans = cluster.KMeans(n_clusters=25, random_state=0).fit(results) # if you get new tweets and run from a new model #1

# kmeans_file = open('clusters.pkl', 'rb') # if you have a model and don't need to train it again #2
# kmeans = pickle.load(kmeans_file) # if you have a model and don't need to train it again #2
# kmeans_file.close() # if you have a model and don't need to train it again #2

count = 1

for label in kmeans.labels_:
    if (label == 1):
        print(count, label) # label is the cluster they're in
    
    count += 1

kmeans_file = open('clusters.pkl', 'wb') # if you get new tweets and run from a new model #1
pickle.dump(kmeans, kmeans_file) # if you get new tweets and run from a new model #1
kmeans_file.close() # if you get new tweets and run from a new model #1
