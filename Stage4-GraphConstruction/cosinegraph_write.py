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
L=48
MIN=-1.19209e-07
MAX=1.9786
DIFF=MAX-MIN

div=4

num="1w"
NUM=10000

def cosineDist(features1, features2):
    """Calculate the cosine distance between two 48 bit features"""
    cosinedist = 1 - np.dot(features1,features2)/(np.linalg.norm(features1)*np.linalg.norm(features2))
    return cosinedist

if __name__ == "__main__":

#nodes
    # featuresfile = h5py.File(os.path.join(__PATH1__, 'features48.hy'), 'r')
    # hyfile_node = h5py.File(os.path.join(__PATH2__,'featurenode'+num+'.hy'), 'w')
    # features=featuresfile["features48"].value
    # features=features[0:NUM]
    # label=featuresfile["originlabel"].value
    # label=label[0:NUM]
    # print features[0],features.shape
    # hyfile_node.create_dataset("featuresnode1"+num,data=features)
    # hyfile_node.create_dataset("featuresnode"+num+"labels",data=label)
    # hyfile_node.close()
    # featuresfile.close()

#relations
    hyfile_node = h5py.File(os.path.join(__PATH2__,'featurenode'+num+'.hy'), 'r')
    hyfile_relation = h5py.File(os.path.join(__PATH2__, 'cosinerelation'+num+'_'+str(div)+'.hy'), 'w')
    features=hyfile_node["featuresnode"+num].value
    features = features[0:NUM]
    label=hyfile_node["featuresnode"+num+"labels"].value
    label=label[0:NUM]
    relations=np.zeros((NUM,NUM))
    precisions=[]
    count=0
    starttime = datetime.datetime.now()
    for i in range(len(features)):
        sameclass = []
        for j in range(len(features)):
            dist = cosineDist(features[i], features[j])
            if i!=j and MAX-DIFF/div<=dist<=MAX:
                print i,j
                relations[i][j]=dist
                issameclass = (label[i] == label[j])
                print label[i],label[j],issameclass,count
                sameclass.append(issameclass)
                count = count + 1
            else:
                relations[i][j]=-1
        sameclass = np.asarray(sameclass, dtype=np.float32)
        if len(sameclass)!=0:
            result=sameclass.min(1)
            precision1 = np.mean(result)
            print("第"+str(i)+"节点的连接准确率："+str(precision1))
            precisions.append(precision1)
    endtime = datetime.datetime.now()
    usetime = (endtime - starttime).seconds
    hyfile_relation.create_dataset("cosinerelation"+num+"_"+str(div),data=relations)
    precisions=np.asarray(precisions,dtype=np.float32)
    print precisions
    precisionresult=np.mean(precisions)
    print precisionresult
    f = file(os.path.join(__PATH2__,'cosineprecisions'+num+'_'+str(div)+'.txt'),"a+")
    f.write('准确率：'+str(precisionresult) + '\n'+'耗时：'+str(usetime)+'\n'+'关系数：'+str(count)+ '\n')
    f.close()
    hyfile_node.close()
    hyfile_relation.close()





