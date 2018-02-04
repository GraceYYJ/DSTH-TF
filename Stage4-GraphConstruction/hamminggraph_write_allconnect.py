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

div=1

num="2w"
NUM=20000
def hammingDist(hashstr1, hashstr2):
    """Calculate the Hamming distance between two bit strings"""
    assert len(hashstr1) == len(hashstr2)
    return sum(c1 != c2 for c1, c2 in zip(hashstr1, hashstr2))

def hammingdist(hasharray1,hasharray2):
    hammingdist = np.sum(hasharray1 != hasharray2)
    return hammingdist

if __name__ == "__main__":
# nodes
#     hashstrfile = h5py.File(os.path.join(__PATH1__, 'predicthasharray.hy'), 'r')
#     hyfile_node = h5py.File(os.path.join(__PATH2__,'hashnodearr'+num+'.hy'), 'w')
#     hashcode=hashstrfile["predicthasharray"].value
#     hashcode=hashcode[0:NUM]
#     label=hashstrfile["originlabel"].value
#     label=label[0:NUM]
#     print hashcode[0],hashcode.shape
#     hyfile_node.create_dataset("hashnodearr"+num,data=hashcode)
#     hyfile_node.create_dataset("hashnodearr"+num+"labels",data=label)
#     hyfile_node.close()
#     hashstrfile.close()

#relations
    hyfile_node = h5py.File(os.path.join(__PATH2__, 'hashnodearr' + num + '.hy'), 'r')
    hyfile_relation = h5py.File(os.path.join(__PATH2__, 'hammingrelationarr' + num + '_' + str(div) + '.hy'), 'w')
    hashcode=hyfile_node["hashnodearr" + num].value
    hashcode=hashcode[0:NUM]
    label=hyfile_node["hashnodearr" + num + "labels"].value
    label=label[0:NUM]
    relations=np.zeros((NUM,NUM))
    precisions=[]
    count=0
    starttime = datetime.datetime.now()
    for i in range(len(hashcode)):
        sameclass = []
        for j in range(len(hashcode)):
            dist = hammingdist(hashcode[i], hashcode[j])
            # if (i!=j) and (dist < L/div):
            if (i != j):
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
    hyfile_relation.create_dataset("hammingrelationarr" + num + "_" + str(div), data=relations)
    precisions=np.asarray(precisions,dtype=np.float32)
    print precisions
    precisionresult=np.mean(precisions)
    print precisionresult
    f = file(os.path.join(__PATH2__,'hammingprecisionsarr'+ num + '_' + str(div) +'.txt'), "a+")
    f.write('准确率：'+str(precisionresult) + '\n'+'耗时：'+str(usetime)+'\n'+'关系数：'+str(count)+ '\n')
    f.close()
    hyfile_node.close()
    hyfile_relation.close()





