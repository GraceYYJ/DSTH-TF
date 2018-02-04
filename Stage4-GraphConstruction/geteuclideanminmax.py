# coding: utf-8
import csv
import time
import h5py
import os.path
import numpy as np
import datetime
#from neo4j.v1 import GraphDatabase, basic_auth
__PATH1__ = '../datasets/cifar10'
__PATH2__ = '../graphfile'
NUM=10000
L=48
def euclideanDist(features1, features2):
    """Calculate the cosine distance between two 48 bit features"""
    euclideandist = np.linalg.norm(features1 - features2)
    return euclideandist

if __name__ == "__main__":

#relations
    hyfile_node1w = h5py.File(os.path.join(__PATH2__,'featurenode1w.hy'), 'r')
    features=hyfile_node1w["featuresnode1w"].value
    features = features[0:NUM]
    print len(features)
    relations_2=np.zeros((NUM,NUM))
    count=0
    distances=[]
    for i in range(len(features)):
        for j in range(len(features)):
            dist = euclideanDist(features[i], features[j])
            distances.append(dist)
    distances=np.asarray(distances,dtype=np.float32)
    min=distances.min()
    max=distances.max()
    print min,max

    f = file(os.path.join(__PATH2__,'euclideanminmax.txt'),"a+")
    f.write('min：'+str(min) + '\n'+'max：'+str(max)+'\n')
    f.close()
    hyfile_node1w.close()





