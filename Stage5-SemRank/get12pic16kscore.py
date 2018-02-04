import os.path
import h5py
import numpy as np
topnum=100

__PATH__ = '../datasets/12pics'
__PATH2__='../SemRank/16k'
__PATH3__='../pickpics16k'

def hammingDist(hashstr1, hashstr2):
    """Calculate the Hamming distance between two bit strings"""
    return sum(c1 != c2 for c1, c2 in zip(hashstr1, hashstr2))

print(["===================read 12picshashcodes.hy"])
hashstr12file = h5py.File(os.path.join(__PATH__, 'predicthashstr.hy'), 'r')
hashstr12=hashstr12file["predicthashstr"].value
print hashstr12,len(hashstr12)

print(["===================read 16khashcodes.hy"])
hashnode16kfile = h5py.File(os.path.join(__PATH3__, 'hashnode16k.hy'), 'r')
hashnode16k=hashnode16kfile["hashnodestr16k"].value
hashnode16klabel=hashnode16kfile["hashnodestr16klabels"].value
print hashnode16k,len(hashnode16k)

print(["===================read Result16k_11.hy"])
Result16k_11file = h5py.File(os.path.join(__PATH2__, 'Result16k_11.hy'), 'r')
Result16k_11=Result16k_11file["Result"].value
Result16k_11.flatten()
print Result16k_11,len(Result16k_11)
print(["===================read sortresult16k.hy"])
sortresult16kfile=h5py.File(os.path.join(__PATH2__, 'sortresult16k.hy'), 'r')
sortresult16k=sortresult16kfile["sortresult16k"].value
print sortresult16k,len(sortresult16k)

def getRank(value,sortresult):
    for i in range(len(sortresult)):
        if value>=sortresult[i]:
            return i
    return -1

meanresult=[]
sum1=0
count=0
for i in range(len(hashstr12)):
    sum1=0
    count = 0
    for j in range(len(hashnode16k)):
        dist=hammingDist(hashstr12[i], hashnode16k[j])
        if dist<=12:
            print hashstr12[i], hashnode16k[j]
            print Result16k_11[j],"   ",hashnode16klabel[j]
            sum1=sum1+Result16k_11[j]
            count=count+1
    if(sum1==0 or count==0):
        mean=0
    else:
        mean=sum1/count
    meanresult.append(mean)

print meanresult

rank=[]
for i in range(len(meanresult)):
    rankx=getRank(meanresult[i],sortresult16k)
    rank.append(rankx)

print rank

hashstr12file.close()
hashnode16kfile.close()
Result16k_11file.close()
sortresult16kfile.close()