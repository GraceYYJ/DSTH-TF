import os.path
import h5py
import numpy as np
topnum=100

__PATH__ = '../datasets/cifar10'
__PATH2__ = '../graphfile'
__PATH3__='../SemRank/1w'
__PATH4__='../SemRank/tencent/2w'

print(["===================read result.hy"])
Resultfile = h5py.File(os.path.join(__PATH4__, 'Result2w_11.hy'), 'r')
Result=Resultfile["Result"].value
print Result,len(Result)
Result2=Result.flatten()
print Result2

sortResultindex=np.argsort(-Result2)
print sortResultindex
sortResultindexfile=h5py.File(os.path.join(__PATH4__, 'sortindex2w.hy'), 'w')
sortResultindexfile.create_dataset("sortindex2w",data=sortResultindex)
sortResultindexfile.close()
print Result2[sortResultindex]
sortResult=Result2[sortResultindex]
sortResultfile=h5py.File(os.path.join(__PATH4__, 'sortresult2w.hy'), 'w')
sortResultfile.create_dataset("sortresult2w",data=sortResult)
sortResultfile.close()
Resultfile.close()

# print(["===================read sortindex2w.hy"])
# Resultfile = h5py.File(os.path.join(__PATH4__, 'sortindex2w.hy'), 'r')
# Result=Resultfile["sortindex2w"].value
# print Result,len(Result)
# f = file(os.path.join(__PATH4__, '2WTOP100.txt'), "a+")
# for i in range(len(Result)):
#     print Result[i]
#     f.write(str(Result[i]) + '\n')
# f.close()


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
