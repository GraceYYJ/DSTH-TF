import os.path
import h5py
import numpy as np
num = 100

__PATH__ = '../datasets/cifar10'
__PATH2__ = '../datasets/pickpics'

print(["===================read data.hy"])
f = h5py.File(os.path.join(__PATH__, 'data.hy'), 'r')
# hash=h5py.File(os.path.join(__PATH__,'hashcode.hy'), 'r')
data18000=h5py.File(os.path.join(__PATH2__,'data18000.hy'), 'w')
id18000 = open(os.path.join(__PATH2__,'id18000.txt'), 'w')
# hashcode=hash["hashcode"].value
hashlabel=[]
count = 0
count0 = 0
count3 = 0

count1 = 0
count2 = 0
count4=0
count5=0
count6=0
count7=0
count8=0
count9=0

for key in f.keys():
    image = f[key]['image'].value
    label = f[key]['label'].value
    if label[0] and count0 < 5000:
        print count0, label
        id18000.write(str(count) + '\n')
        grp=data18000.create_group(str(count))
        grp['image']=image
        grp['label']=label
        # hashlabel.append(hashcode[count])
        count0 = count0 + 1
        count = count + 1
    if label[3] and count3 < 3000:
        print count3, label
        id18000.write(str(count) + '\n')
        grp=data18000.create_group(str(count))
        grp['image']=image
        grp['label']=label
        # hashlabel.append(hashcode[count])
        count3 = count3 + 1
        count = count + 1
    if label[1] and count1 < 1000:
        print count1, label
        id18000.write(str(count) + '\n')
        grp=data18000.create_group(str(count))
        grp['image']=image
        grp['label']=label
        # hashlabel.append(hashcode[count])
        count1 = count1 + 1
        count = count + 1
    if label[2] and count2 < 1000:
        print count1, label
        id18000.write(str(count) + '\n')
        grp=data18000.create_group(str(count))
        grp['image']=image
        grp['label']=label
        # hashlabel.append(hashcode[count])
        count2 = count2 + 1
        count = count + 1
    if label[4] and count4 < 1000:
        print count4, label
        id18000.write(str(count) + '\n')
        grp=data18000.create_group(str(count))
        grp['image']=image
        grp['label']=label
        # hashlabel.append(hashcode[count])
        count4 = count4 + 1
        count = count + 1
    if label[5] and count5 < 1000:
        print count1, label
        id18000.write(str(count) + '\n')
        grp=data18000.create_group(str(count))
        grp['image']=image
        grp['label']=label
        # hashlabel.append(hashcode[count])
        count5 = count5 + 1
        count = count + 1
    if label[6] and count6 < 1000:
        print count6, label
        id18000.write(str(count) + '\n')
        grp=data18000.create_group(str(count))
        grp['image']=image
        grp['label']=label
        # hashlabel.append(hashcode[count])
        count6 = count6 + 1
        count = count + 1
    if label[7] and count7 < 1000:
        print count7, label
        id18000.write(str(count) + '\n')
        grp=data18000.create_group(str(count))
        grp['image']=image
        grp['label']=label
        # hashlabel.append(hashcode[count])
        count7 = count7 + 1
        count = count + 1
    if label[8] and count8 < 1000:
        print count8, label
        id18000.write(str(count) + '\n')
        grp=data18000.create_group(str(count))
        grp['image']=image
        grp['label']=label
        # hashlabel.append(hashcode[count])
        count8 = count8 + 1
        count = count + 1
    if label[9] and count9 < 1000:
        print count8, label
        id18000.write(str(count) + '\n')
        grp = data18000.create_group(str(count))
        grp['image'] = image
        grp['label'] = label
        # hashlabel.append(hashcode[count])
        count9 = count9 + 1
        count = count + 1


# hashlabel=np.asarray(hashlabel,dtype=np.float32)
# dset=data18000.create_dataset("hashlabel",data=hashlabel)
print count,count0,count3,count1,count2,count4,count5,count6,count7,count8,count9

data18000.close()
id18000.close()
# hash.close()
f.close()

