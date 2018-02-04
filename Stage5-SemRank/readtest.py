import os.path
import h5py
import numpy as np
num=100

__PATH__ = '../datasets/cifar10'
__PATH2__ = '../graphfile'
__PATH3__='../SemRank/16k'
__PATH4__ = '../pickpics16k'
# print(["===================read hash.hy"])
# f = h5py.File(os.path.join(__PATH__, 'hash.hy'), 'r')
# for key in f.keys():
#     print(f[key].name)
    # for key2 in f[key].keys():
    #     print f[key][key2].name
    #     print f[key][key2].value
# f.close()

# print(["===================read data.hy"])
# f = h5py.File(os.path.join(__PATH__, 'data.hy'), 'r')
# for key in f.keys():
#     print(f[key].name)
#     for key2 in f[key].keys():
#         print f[key][key2].name
#         print f[key][key2].value
#         print f[key][key2].value.shape
# f.close()

# print(["===================read features.hy"])
# f = h5py.File(os.path.join(__PATH__, 'features.hy'), 'r')
# print f["features"].name
# print f["features"].value
# print f["features"].value.shape
# f.close()

# print(["===================read hashcode.hy"])
# f = h5py.File(os.path.join(__PATH__, 'hashcode.hy'), 'r')
# print f["hashcode"].name
# print f["hashcode"].value
# print f["hashcode"].value.shape
# f.close()

# print(["===================read data10000.hy"])
# f = h5py.File(os.path.join(__PATH__, 'data10000.hy'), 'r')
# for key in f.keys():
#     print(f[key].name)
#     for key2 in f[key].keys():
#         print f[key][key2].name
#         print f[key][key2].value
# f.close()

# print(["===================read predicthashstr.hy"])
# f = h5py.File(os.path.join(__PATH__, 'predicthashstr.hy'), 'r')
# print f["predicthashstr"].value
# print f["predicthashstr"].value.shape
# print f["originlabel"].value
# print f["originlabel"].value.shape
# f.close()

# print(["===================read features48.hy"])
# f = h5py.File(os.path.join(__PATH__, 'features48.hy'), 'r')
# print f["features48"].value
# print f["features48"].value.shape
# print f["originlabel"].value
# print f["originlabel"].value.shape
# f.close()

# print(["===================read features48.hy"])
# f = h5py.File(os.path.join(__PATH2__, 'relation1w_2.hy'), 'r')
# print f["relation1w_2"].value
# print f["relation1w_2"].value.shape
# f.close()

# print(["===================read node1w.hy"])
# NUM=10000
# hyfile_node1w = h5py.File(os.path.join(__PATH2__, 'node1w.hy'), 'r')
# hashcode = hyfile_node1w["node1w"].value
# hashcode = hashcode[0:NUM]
# label = hyfile_node1w["node1wlabels"].value
# label = label[0:NUM]
# print hashcode
# print label
# y=[]
# x1=(label[1]==label[2])
# y.append(x1)
# x2=(label[0]==label[2])
# y.append(x2)
# print y
# y=np.asarray(y,dtype=np.float32)
# print y
# result=y.min(1)
# print result

# print(["===================read hammingrelation1w_2.hy"])
# f = h5py.File(os.path.join(__PATH2__, 'hammingrelation1w_2.hy'), 'r')
# for key in f.keys():
#     print(f[key].name)
# f.close()

# print(["===================read hashnode16khy"])
# number="16k"
# hyfile_node = h5py.File(os.path.join(__PATH4__, 'hashnode' + number + '.hy'), 'r')
# # for key in hyfile_node.keys():
# #     print(hyfile_node[key].name)
# hashlabel=hyfile_node["hashnodestr" + number +"labels"]
# print hashlabel[9375],hashlabel[6923],hashlabel[6387],hashlabel[13307]
# hyfile_node.close()

print(["===================read result.hy"])
Result1w_7_file = h5py.File(os.path.join(__PATH3__, 'Result16k_11.hy'), 'r')
sum=0
Result=Result1w_7_file["Result"].value
print Result,len(Result)
for i in range(len(Result)):
    sum=Result[i][0]+sum
print sum
Result1w_7_file.close()