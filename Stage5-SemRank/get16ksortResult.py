import os.path
import h5py
import numpy as np
topnum=100

__PATH2__ = '../pickpics16k'
__PATH4__='../SemRank/16k'

print(["===================read result.hy"])
Resultfile = h5py.File(os.path.join(__PATH4__, 'Result16k_11.hy'), 'r')
Result=Resultfile["Result"].value
print Result,len(Result)
Result2=Result.flatten()
print Result2

sortResultindex=np.argsort(-Result2)
print sortResultindex
sortResultindexfile=h5py.File(os.path.join(__PATH4__, 'sortindex16k.hy'), 'w')
sortResultindexfile.create_dataset("sortindex16k",data=sortResultindex)
sortResultindexfile.close()
print Result2[sortResultindex]

sortResult=Result2[sortResultindex]
sortResultfile=h5py.File(os.path.join(__PATH4__, 'sortresult16k.hy'), 'w')
sortResultfile.create_dataset("sortresult16k",data=sortResult)
sortResultfile.close()
Resultfile.close()

print(["===================read sortindex16k.hy"])
Resultfile = h5py.File(os.path.join(__PATH4__, 'sortindex16k.hy'), 'r')
Result=Resultfile["sortindex16k"].value
print Result,len(Result)
Result=Result[0:topnum]
f = file(os.path.join(__PATH4__, '2WTOP'+str(topnum)+'.txt'), "a+")
for i in range(len(Result)):
    print Result[i]
    f.write(str(i)+": "+str(Result[i]) + "\n")
f.close()


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
