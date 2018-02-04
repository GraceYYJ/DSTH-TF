# coding: utf-8
import csv
import time
import h5py
import os.path
import numpy as np
import datetime
#from neo4j.v1 import GraphDatabase, basic_auth
__PATH1__ = '../datasets/pickpics'
__PATH2__ = '../pickpics16k'
L=48

div=2

num="cat2100"
NUM=3000
def hammingDist(hashstr1, hashstr2):
    """Calculate the Hamming distance between two bit strings"""
    return sum(c1 != c2 for c1, c2 in zip(hashstr1, hashstr2))

def hammingdist(hasharray1,hasharray2):
    hammingdist = np.sum(hasharray1 != hasharray2)
    return hammingdist

if __name__ == "__main__":
# nodes
    hashstrfile = h5py.File(os.path.join(__PATH1__, 'datacatnum100.hy'), 'r')
    hyfile_node = h5py.File(os.path.join(__PATH2__,'hashnode'+num+'.hy'), 'w')
    hashcode=hashstrfile["pickedhashcode"].value
    label=hashstrfile["pickedlabel"].value
    hyfile_node.create_dataset("hashnodestr"+num,data=hashcode)
    hyfile_node.create_dataset("hashnodestr"+num+"labels",data=label)
    hyfile_node.close()
    hashstrfile.close()

#relations
    hyfile_node = h5py.File(os.path.join(__PATH2__, 'hashnode' + num + '.hy'), 'r')
    hyfile_relation = h5py.File(os.path.join(__PATH2__, 'hammingrelation' + num + '_' + str(div) + '.hy'), 'w')
    hashcode=hyfile_node["hashnodestr" + num].value
    label=hyfile_node["hashnodestr" + num + "labels"].value
    relations=np.zeros((NUM,NUM))
    precisions=[]
    count=0
    starttime = datetime.datetime.now()
    for i in range(len(hashcode)):
        sameclass = []
        for j in range(len(hashcode)):
            dist = hammingDist(hashcode[i], hashcode[j])
            if (i!=j) and (dist < L/div):
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
    hyfile_relation.create_dataset("hammingrelation" + num + "_" + str(div), data=relations)
    precisions=np.asarray(precisions,dtype=np.float32)
    print precisions
    precisionresult=np.mean(precisions)
    print precisionresult
    f = file(os.path.join(__PATH2__,'hammingprecisions'+ num + '_' + str(div) +'.txt'), "a+")
    f.write('准确率：'+str(precisionresult) + '\n'+'耗时：'+str(usetime)+'\n'+'关系数：'+str(count)+ '\n')
    f.close()
    hyfile_node.close()
    hyfile_relation.close()





