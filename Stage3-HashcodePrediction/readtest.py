import os.path
import h5py
num=100

__PATH__ = '../datasets/cifar10'
__PATH2__ = '../datasets/tencentdata'
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

print(["===================read tencentdata.hy"])
f = h5py.File(os.path.join(__PATH2__, 'tencentdata.hy'), 'r')
for key in f.keys():
    print(f[key].name)
    for key2 in f[key].keys():
        print f[key][key2].name
        print f[key][key2].value
        print f[key][key2].value.shape
f.close()