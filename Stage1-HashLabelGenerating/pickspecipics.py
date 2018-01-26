import os.path
import h5py
import numpy as np
num = 100

__PATH__ = '../datasets/cifar10'

print(["===================read data.hy"])
f = h5py.File(os.path.join(__PATH__, 'data.hy'), 'r')
hash=h5py.File(os.path.join(__PATH__,'hashcode.hy'), 'r')
data10000=h5py.File(os.path.join(__PATH__,'data10000.hy'), 'w')
id10000 = open(os.path.join(__PATH__,'id10000.txt'), 'w')
hashcode=hash["hashcode"].value
hashlabel=[]
count = 0
count1 = 0
count2 = 0
count3 = 0
for key in f.keys():
    image = f[key]['image'].value
    label = f[key]['label'].value
    if label[0] and count1 < 6000:
        print count1, label
        id10000.write(str(count) + '\n')
        grp=data10000.create_group(str(count))
        grp['image']=image
        grp['label']=label
        hashlabel.append(hashcode[count])
        count1 = count1 + 1
        count = count + 1
    if label[1] and count2 < 3000:
        print count2, label
        id10000.write(str(count) + '\n')
        grp=data10000.create_group(str(count))
        grp['image']=image
        grp['label']=label
        hashlabel.append(hashcode[count])
        count2 = count2 + 1
        count = count + 1
    if label[2] and count3 < 1000:
        print count3, label
        id10000.write(str(count) + '\n')
        grp=data10000.create_group(str(count))
        grp['image']=image
        grp['label']=label
        hashlabel.append(hashcode[count])
        count3 = count3 + 1
        count = count + 1
hashlabel=np.asarray(hashlabel,dtype=np.float32)
dset=data10000.create_dataset("hashlabel",data=hashlabel)
print count1, count2, count3,count
data10000.close()
id10000.close()
hash.close()
f.close()

