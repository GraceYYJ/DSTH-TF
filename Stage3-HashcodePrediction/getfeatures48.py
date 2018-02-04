# -*- coding:utf-8 -*-
import argparse
import tensorflow as tf
import utils
import datetime
import numpy as np
import h5py
import os.path

__PATH__ = '../datasets/cifar10'
batchsize=100

def load_graph(frozen_graph_filename):
    # We parse the graph_def file
    with tf.gfile.GFile(frozen_graph_filename, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
    # fix nodes
    for node in graph_def.node:
        if node.op == 'RefSwitch':
            node.op = 'Switch'
            for index in xrange(len(node.input)):
                if 'moving_' in node.input[index]:
                    node.input[index] = node.input[index] + '/read'
        elif node.op == 'AssignSub':
            node.op = 'Sub'
            if 'use_locking' in node.attr: del node.attr['use_locking']

        # We load the graph_def in the default graph
    with tf.Graph().as_default() as graph:
        tf.import_graph_def(graph_def,name='')
    return graph


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--frozen_model_filename", default="/tfproject/DSTH-TF/classifymodel/checkpoint/cifar10_50_32_32/classify_model.pb", type=str,
                        help="Frozen model file to import")
    args = parser.parse_args()
    graph = load_graph(args.frozen_model_filename)

    # We can list operations
    # op.values() gives you a list of tensors it produces
    # op.name gives you the name

    for op in graph.get_operations():
        print(op.name, op.values())

        # prefix/Placeholder/inputs_placeholder
        # ...
        # prefix/Accuracy/predictions

    features=[]
    starttime = datetime.datetime.now()
    inputs=graph.get_tensor_by_name('images:0')
    #predictions=graph.get_tensor_by_name('Accuracy/predictions:0')
    fc4=graph.get_tensor_by_name('network32/n_fc_4/add:0')
    ids, labels, images = utils.getidsAndimages('/tfproject/DSTH-TF/datasets/cifar10')
    #hashtags=utils.getHashtags('/tfproject/DSTH-TF/datasets/cifar10')
    batch_idxs = len(ids) // batchsize
    with tf.Session(graph=graph) as sess:
        for idx in xrange(0, batch_idxs):
            batch1 = images[idx * batchsize:(idx + 1) * batchsize]
            batch_images = np.array(batch1).astype(np.float32)
            features48 = sess.run(fc4, feed_dict={inputs:batch_images})
            print(features48)  # [[ 0.]] Yay!
            features.extend(features48)
        features = np.asarray(features, dtype=np.float32)
        print features
        print features.shape
        predictfeatures48 = h5py.File(os.path.join(__PATH__, 'features48.hy'), 'w')
        predictfeatures48.create_dataset("features48", data=features)
        predictfeatures48.create_dataset("originlabel", data=labels)
    print ("finish")
    endtime = datetime.datetime.now()
    usetime=(endtime-starttime).seconds
    print usetime,"seconds"

    predictfeatures48.close()