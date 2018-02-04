import os.path
import h5py
num=100

__PATH__ = '../datasets/cifar10'
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

# print(["===================read predicthashs.hy"])
# f = h5py.File(os.path.join(__PATH__, 'predicthashs.hy'), 'r')
# print f["predicthashs"].name
# print f["predicthashs"].value
# print f["predicthashs"].value.shape
# f.close()

print(["===================read data18000.hy"])
f = h5py.File(os.path.join(__PATH__, 'data18000.hy'), 'r')
for key in f.keys():
    print f[key].name
    # for key2 in f[key].keys():
    #     print f[key][key2].name
    #     print f[key][key2].value
    #     print f[key][key2].value.shape
f.close()