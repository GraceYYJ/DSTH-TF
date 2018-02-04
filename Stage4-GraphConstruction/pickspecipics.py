import os.path
import h5py
import numpy as np
__PATH__ = '../datasets/cifar10'
__PATH2__ = '../datasets/pickpics'
catnum=2100
print(["===================read data.hy"])
f = h5py.File(os.path.join(__PATH__, 'predicthashstr.hy'), 'r')
# hash=h5py.File(os.path.join(__PATH__,'hashcode.hy'), 'r')
hashcode=f["predicthashstr"].value
label=f["originlabel"].value
pickedhashcode=[]
pickedlabel=[]
count = 0
count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4=0
count5=0
count6=0
count7=0
count8=0
count9=0

for i in range(len(hashcode)):
    if label[i][0]==1 and count0 < 100:
        print count0, hashcode[i],label[i]
        pickedhashcode.append(hashcode[i])
        pickedlabel.append(label[i])
        count0 = count0 + 1
        count = count + 1
    if label[i][1]==1 and count1 < 100:
        print count3, hashcode[i],label[i]
        pickedhashcode.append(hashcode[i])
        pickedlabel.append(label[i])
        count1 = count1 + 1
        count = count + 1
    if label[i][2]==1 and count2 < 100:
        print count1, hashcode[i],label[i]
        pickedhashcode.append(hashcode[i])
        pickedlabel.append(label[i])
        count2 = count2 + 1
        count = count + 1
    if label[i][3]==1and count3 < 2100:
        print count1, hashcode[i],label[i]
        pickedhashcode.append(hashcode[i])
        pickedlabel.append(label[i])
        count3 = count3 + 1
        count = count + 1
    if label[i][4]==1and count4 < 100:
        print count4, hashcode[i],label[i]
        pickedhashcode.append(hashcode[i])
        pickedlabel.append(label[i])
        count4 = count4 + 1
        count = count + 1
    if label[i][5]==1 and count5 < 100:
        print count1, hashcode[i],label[i]
        pickedhashcode.append(hashcode[i])
        pickedlabel.append(label[i])
        count5 = count5 + 1
        count = count + 1
    if label[i][6]==1 and count6 < 100:
        print count6, hashcode[i],label[i]
        pickedhashcode.append(hashcode[i])
        pickedlabel.append(label[i])
        count6 = count6 + 1
        count = count + 1
    if label[i][7]==1 and count7 < 100:
        print count7, hashcode[i],label[i]
        pickedhashcode.append(hashcode[i])
        pickedlabel.append(label[i])
        count7 = count7 + 1
        count = count + 1
    if label[i][8]==1 and count8 < 100:
        print count8, hashcode[i],label[i]
        pickedhashcode.append(hashcode[i])
        pickedlabel.append(label[i])
        count8 = count8 + 1
        count = count + 1
    if label[i][9]==1 and count9 < 100:
        print count8, hashcode[i],label[i]
        pickedhashcode.append(hashcode[i])
        pickedlabel.append(label[i])
        count9 = count9 + 1
        count = count + 1

print count,count0,count2,count2,count3,count4,count5,count6,count7,count8,count9
pickedhashcode=np.asarray(pickedhashcode)
pickedlabel=np.asarray(pickedlabel)
print pickedhashcode,pickedhashcode.shape
print pickedlabel,pickedlabel.shape
pickeddata=h5py.File(os.path.join(__PATH2__,'datacatnum'+str(catnum)+'.hy'), 'w')
pickeddata.create_dataset("pickedhashcode",data=pickedhashcode)
pickeddata.create_dataset("pickedlabel",data=pickedlabel)
pickeddata.close()
f.close()

