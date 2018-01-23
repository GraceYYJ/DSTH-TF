# -*- coding:utf-8 -*-
import argparse
import tensorflow as tf
import utils


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
    parser.add_argument("--frozen_model_filename", default="/tfproject/DSTH-TF/checkpoint/cifar10_50_32_32/frozen_model.pb", type=str,
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

    inputs=graph.get_tensor_by_name('images:0')
    #hashtags=graph.get_tensor_by_name('hashbit:0')
    logits=graph.get_tensor_by_name('Accuracy/predictions:0')

    ids, _, images = utils.getidsAndimages('/tfproject/DSTH-TF/datasets/cifar10')
    hashs = utils.getHashtags('/tfproject/DSTH-TF/datasets/cifar10')
    print hashs[0]
    with tf.Session(graph=graph) as sess:
        hashcode = sess.run(logits, feed_dict={inputs:images[0:50]})
        print(hashcode)  # [[ 0.]] Yay!
    print ("finish")