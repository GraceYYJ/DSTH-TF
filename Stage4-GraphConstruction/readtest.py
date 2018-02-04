import os.path
import h5py
import numpy as np
num=100

__PATH__ = '../datasets/cifar10'
__PATH2__ = '../graphfile'
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

# print(["===================read consinerelation1w_2.hy"])
# f = h5py.File(os.path.join(__PATH2__, 'consinerelation1w_2.hy'), 'r')
# print f["cosinerelation1w_2"].value
# print f["cosinerelation1w_2"].value.shape
# f.close()

# print(["===================read hashnode2w.hy"])
# num="2w"
# hyfile_node = h5py.File(os.path.join(__PATH2__, 'hashnode' + num + '.hy'), 'r')
# print
# for key in hyfile_node.keys():
#     print(hyfile_node[key].name)
# hyfile_node.close()

print(["===================read featuresnode2w.hy"])
num="2w"
hyfile_node = h5py.File(os.path.join(__PATH2__, 'featurenode' + num + '.hy'), 'r')
print
for key in hyfile_node.keys():
    print(hyfile_node[key].name)
hyfile_node.close()