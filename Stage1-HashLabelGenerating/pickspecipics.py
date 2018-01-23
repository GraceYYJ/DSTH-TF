import os.path
import h5py

num = 100

__PATH__ = '../datasets/cifar10'

print(["===================read data.hy"])
f = h5py.File(os.path.join(__PATH__, 'data.hy'), 'r')
data10000=h5py.File(os.path.join(__PATH__,'data10000.hy'), 'w')
count = 0
count1 = 0
count2 = 0
count3 = 0
for key in f.keys():
    image = f[key]['image'].value
    label = f[key]['label'].value
    if label[0] and count1 < 6000:
        print count1, label
        grp=data10000.create_group(str(count))
        grp['image']=image
        grp['label']=label
        count1 = count1 + 1
        count = count + 1
    if label[1] and count2 < 3000:
        print count2, label
        grp=data10000.create_group(str(count))
        grp['image']=image
        grp['label']=label
        count2 = count2 + 1
        count = count + 1
    if label[2] and count3 < 1000:
        print count3, label
        grp=data10000.create_group(str(count))
        grp['image']=image
        grp['label']=label
        count3 = count3 + 1
        count = count + 1
print count1, count2, count3,count
data10000.close()
f.close()

