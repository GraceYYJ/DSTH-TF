from __future__ import division
import skimage
import skimage.io
import skimage.transform
import numpy as np
import os.path
import h5py
import math
import json
import random
import pprint
import scipy.misc
import numpy as np
from time import gmtime, strftime
from six.moves import xrange

import tensorflow as tf
import tensorflow.contrib.slim as slim

pp = pprint.PrettyPrinter()
get_stddev = lambda x, k_h, k_w: 1/math.sqrt(k_w*k_h*x.get_shape()[-1])

def show_all_variables():
  model_vars = tf.trainable_variables()
  slim.model_analyzer.analyze_vars(model_vars, print_info=True)

def load_image(path):
    img = skimage.io.imread(path)
    img = img / 255.0
    assert (0 <= img).all() and (img <= 1.0).all()
    # print "Original Image Shape: ", img.shape
    # we crop image from center
    short_edge = min(img.shape[:2])
    yy = int((img.shape[0] - short_edge) / 2)
    xx = int((img.shape[1] - short_edge) / 2)
    crop_img = img[yy: yy + short_edge, xx: xx + short_edge]
    # resize to 224, 224
    resized_img = skimage.transform.resize(crop_img, (224, 224))
    return resized_img

def load_image2(path, height=None, width=None):
    # load image
    img = skimage.io.imread(path)
    img = img / 255.0
    if height is not None and width is not None:
        ny = height
        nx = width
    elif height is not None:
        ny = height
        nx = img.shape[1] * ny / img.shape[0]
    elif width is not None:
        nx = width
        ny = img.shape[0] * nx / img.shape[1]
    else:
        ny = img.shape[0]
        nx = img.shape[1]
    return skimage.transform.resize(img, (ny, nx))

def load_image3(img):
    resized_img = skimage.transform.resize(img, (224, 224))
    return resized_img

def getidsAndimages(dataset_name):
    id_txt = os.path.join('../datasets',dataset_name,'id.txt')
    try:
        with open(id_txt, 'r') as fp:
            ids = [s.strip() for s in fp.readlines() if s]
    except:
        raise IOError('Dataset not found. Please make sure the dataset was downloaded.')
    file = os.path.join('../datasets',dataset_name,'data.hy')
    try:
        data = h5py.File(file, 'r')
    except:
        raise IOError('Dataset not found. Please make sure the dataset was downloaded.')
    images=[]
    for i in range(len(ids)):
        image = data[ids[i]]['image'].value / 255.
        images.append(image.astype(np.float32))
    images=np.asarray(images, dtype=np.float32)
    data.close()
    print("images",images.shape)
    return ids,data,images

def getHashtags(dataset_name):
    f = h5py.File(os.path.join('../datasets',dataset_name, 'hashcode.hy'), 'r')
    hashtags=f["hashcode"].value
    return hashtags
    f.close()
