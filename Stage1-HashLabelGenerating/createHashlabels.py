import datetime
import os.path

import h5py
import numpy as np
import tensorflow as tf
from sklearn import manifold

import utils
import vgg16
from logs import log

'''some parameters'''

batchsize=100
images = tf.placeholder("float", [batchsize, 224, 224, 3])
__PATH__ = '../datasets/cifar10'

def getAllids():
    id_filename = 'id.txt'
    id_txt = os.path.join(__PATH__, id_filename)
    try:
        with open(id_txt, 'r') as fp:
            _ids = [s.strip() for s in fp.readlines() if s]
    except:
        raise IOError('Dataset not found. Please make sure the dataset was downloaded.')
    return _ids

def getData():
    filename = 'data.hy'
    file = os.path.join(__PATH__, filename)
    log.info("Reading %s ...", file)
    try:
        data = h5py.File(file, 'r')
    except:
        raise IOError('Dataset not found. Please make sure the dataset was downloaded.')
    log.info("Reading Done: %s", file)
    return data

def getBatch(totalnum,count,allids,data):
    imagebatch=[]
    for i in range(batchsize):
        if count*batchsize+i<totalnum:
            #print allids[count*batchsize+i]
            image=data[allids[count*batchsize+i]]['image'].value/255.
            image2= utils.load_image3(image)
            imagebatch.append(image2)
    imagebatch=np.asarray(imagebatch, dtype=np.float32)
    print("imagebatch",imagebatch.shape)
    return imagebatch

def getAllImages(ids,data):
    images=[]
    for i in range(len(ids)):
        image = data[ids[i]]['image'].value / 255.
        print("image", image.shape)
        image2= utils.load_image3(image)
        images.append(image2.astype(np.float32))
    images=np.asarray(images, dtype=np.float32)
    print("images",images.shape)
    return images

def createHashTag(features,n_hash, n_neis):
    print ("features:",features.shape)
    lapVecs = manifold.SpectralEmbedding(n_components=n_hash, n_neighbors=n_neis).fit_transform(features)
    hashbool = lapVecs >= 0
    hashtags = hashbool.astype(np.int32)
    print "hashtags:",hashtags
    return hashtags

with tf.Session(
        config=tf.ConfigProto(gpu_options=(tf.GPUOptions(per_process_gpu_memory_fraction=0.7)))) as sess:
    vgg = vgg16.Vgg16()
    with tf.name_scope("content_vgg"):
        vgg.build(images)
    straight = tf.reshape(vgg.pool5, [vgg.pool5.shape[0], -1])
    ids = getAllids()
    data = getData()
    totalnum=len(ids)
    print ("totalnum", totalnum)
    batchnum = totalnum / batchsize
    if (totalnum % batchsize != 0):
        batchnum += 1
    features=[]
    for j in range(batchnum):
        print "the ",j," batch"
        batch = getBatch(totalnum, j, ids, data)
        straightOP = sess.run(straight, feed_dict={images: batch})
        #print("straightOPs:", straightOP.shape)
        features.extend(straightOP)
        #print("features:", len(features))
    features=np.asarray(features,dtype=np.float32)
    featuresh5py=h5py.File(os.path.join(__PATH__,'features.hy'), 'w')
    featuresh5py.create_dataset("features",data=features)

    print("createhashtags")
    featuresfile = h5py.File(os.path.join(__PATH__, 'features.hy'), 'r')
    features=featuresfile["features"].value
    print "features",features
    starttime = datetime.datetime.now()
    hashtags = createHashTag(features, 48, 10)
    print("hashtags:", len(hashtags))
    hashcodeh5py=h5py.File(os.path.join(__PATH__,'hashcode.hy'), 'w')
    hashcodeh5py.create_dataset("hashcode",data=hashtags)

    hashcodeh5py.close()
    featuresfile.close()
    data.close()
    endtime = datetime.datetime.now()
    usetime=(endtime-starttime).seconds
    print usetime,"seconds"

