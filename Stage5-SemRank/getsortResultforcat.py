from __future__ import division
import os.path
import h5py
import numpy as np
topnum1=150
topnum2=600
topnum3=3000
num="cat2100"
NUM=3000
__PATH1__ = '../datasets/pickpics'
__PATH2__ = '../pickpics16k'
__PATH4__='../SemRank/cat/3000'

print(["===================read result.hy"])
Resultfile = h5py.File(os.path.join(__PATH4__, 'Resultcat2100_11.hy'), 'r')
Result=Resultfile["Result"].value
print Result,len(Result)
Result2=Result.flatten()
print Result2

sortResultindex=np.argsort(-Result2)
print sortResultindex
sortResultindexfile=h5py.File(os.path.join(__PATH4__, 'sortindexcat.hy'), 'w')
sortResultindexfile.create_dataset("sortindex",data=sortResultindex)
sortResultindexfile.close()
print Result2[sortResultindex]

sortResult=Result2[sortResultindex]
sortResultfile=h5py.File(os.path.join(__PATH4__, 'sortresult.hy'), 'w')
sortResultfile.create_dataset("sortresult",data=sortResult)
sortResultfile.close()
Resultfile.close()

hashstrfile = h5py.File(os.path.join(__PATH1__, 'datacatnum2100.hy'), 'r')
hashcode = hashstrfile["pickedhashcode"].value
label = hashstrfile["pickedlabel"].value

print(["===================read sortindex.hy"])
Resultfile = h5py.File(os.path.join(__PATH4__, 'sortindexcat.hy'), 'r')
Result=Resultfile["sortindex"].value
print Result,len(Result)
Result1=Result[0:topnum1]
f1 = file(os.path.join(__PATH4__, 'TOP'+str(topnum1)+'.txt'), "a+")
count1=0
count2=0
for i in range(len(Result1)):
    print Result[i], label[Result[i]][3]
    if label[Result[i]][3]==1:
        print count1
        count1=count1+1
    f1.write(str(i)+": "+str(Result[i]) + "--"+str(label[Result[i]][3])+"\n")
print count1
mean = count1 / topnum1
print count1
f1.write(str(count1) + "\n"+str(mean) + "\n")
f1.close()

Result2=Result[0:topnum3]
f2 = file(os.path.join(__PATH4__, 'TOP'+str(topnum3)+'.txt'), "a+")
for i in range(len(Result2)):
    print Result[i],label[Result[i]][3]
    if label[Result[i]][3]==1:
        print count2
        count2=count2+1
    f2.write(str(i)+": "+str(Result[i]) + "--"+str(label[Result[i]][3])+"\n")
print count2
mean = count2 / topnum3
print mean
f2.write(str(count2) + "\n"+str(mean) + "\n")
f2.close()

hashstrfile.close()
# print(["===================read consinerelation1w_2.hy"])
# f = h5py.File(os.path.join(__PATH2__, 'consinerelation1w_2.hy'), 'r')
# print f["cosinerelation1w_2"].value
# print f["cosinerelation1w_2"].value.shape
# f.close()
#
# print(["===================read hashnode5h.hy"])
# num="5h"
# hyfile_node = h5py.File(os.path.join(__PATH2__, 'hashnode' + num + '.hy'), 'r')
# print
# for key in hyfile_node.keys():
#     print(hyfile_node[key].name)
# hyfile_node.close()

# print(["===================read result.hy"])
# Resultfile = h5py.File(os.path.join(__PATH3__, 'Result2w_15.hy'), 'r')
# sum=0
# Result=Result1file["Result"].value
# print Result,len(Result)
# for i in range(len(Result)):
#     sum=Result[i][0]+sum
# print sum
# Resultfile.close()
