# -*- coding:utf-8 -*-
import os, argparse
import tensorflow as tf
from tensorflow.python.framework import graph_util

dir = os.path.dirname(os.path.realpath(__file__))


def freeze_graph(model_folder):
    # We retrieve our checkpoint fullpath
    checkpoint = tf.train.get_checkpoint_state(model_folder)
    input_checkpoint = checkpoint.model_checkpoint_path
    print input_checkpoint
    # We precise the file fullname of our freezed graph
    absolute_model_folder = "/".join(input_checkpoint.split('/')[:-1])
    output_graph = absolute_model_folder + "/frozen_model.pb"
    #output_graph = absolute_model_folder + "/classify_model.pb"
    # output_node_names = "Accuracy/predictions"
    output_node_names = "network32/n_fc_4/add"

    # We clear the devices, to allow TensorFlow to control on the loading where it wants operations to be calculated
    clear_devices = True

    # We import the meta graph and retrive a Saver
    saver = tf.train.import_meta_graph(input_checkpoint + '.meta', clear_devices=clear_devices)

    # We retrieve the protobuf graph definition
    graph = tf.get_default_graph()
    input_graph_def = graph.as_graph_def()

    # We start a session and restore the graph weights
    with tf.Session() as sess:
        saver.restore(sess, input_checkpoint)
        # fix batch norm nodes
        for node in input_graph_def.node:
            if node.op == 'RefSwitch':
                node.op = 'Switch'
                for index in xrange(len(node.input)):
                    if 'moving_' in node.input[index]:
                        node.input[index] = node.input[index] + '/read'
            elif node.op == 'AssignSub':
                node.op = 'Sub'
                if 'use_locking' in node.attr: del node.attr['use_locking']

        # We use a built-in TF helper to export variables to constant
        output_graph_def = graph_util.convert_variables_to_constants(
            sess,
            input_graph_def,
            output_node_names.split(",")  # We split on comma for convenience
        )
        # Finally we serialize and dump the output graph to the filesystem
        with tf.gfile.GFile(output_graph, "wb") as f:
            f.write(output_graph_def.SerializeToString())
        print("%d ops in the final graph." % len(output_graph_def.node))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_folder", type=str, help="Model folder to export")
    args = parser.parse_args()

    freeze_graph(args.model_folder)