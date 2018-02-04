import numpy as np
import tensorflow as tf

import vgg16
import utils
import pickle

#img1 = utils.load_image("./test_data/tiger.jpeg")
#img2 = utils.load_image("./test_data/puzzle.jpeg")


#batch1 = img1.reshape((1, 224, 224, 3))
#batch2 = img2.reshape((1, 224, 224, 3))

#batch = np.concatenate((batch1, batch2), 0)

def load_file(filename):
    with open(filename, 'rb') as fo:
        data = pickle.load(fo, encoding='latin1')
    return data

with tf.Session(
        config=tf.ConfigProto(gpu_options=(tf.GPUOptions(per_process_gpu_memory_fraction=0.7)))) as sess:
    data = load_file('test_batch')
    images = tf.placeholder("float", [2, 224, 224, 3])
    feed_dict = {images: batch}

    vgg = vgg16.Vgg16()
    #print vgg.data_dict["prob"][0]
    with tf.name_scope("content_vgg"):
        vgg.build(images)
    pool5=sess.run(vgg.pool5, feed_dict=feed_dict)
    print(pool5.shape)
    print pool5
    straight=sess.run(vgg.straight, feed_dict=feed_dict)
    print(straight.shape)
    print straight

    #prob = sess.run(vgg.prob, feed_dict=feed_dict)
    #print(prob.shape)
    #utils.print_prob(prob[0], './synset.txt')
    #utils.print_prob(prob[1], './synset.txt')
