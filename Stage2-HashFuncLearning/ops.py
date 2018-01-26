import math
import numpy as np 
import tensorflow as tf

from tensorflow.python.framework import ops

from utils import *

try:
  image_summary = tf.image_summary
  scalar_summary = tf.scalar_summary
  histogram_summary = tf.histogram_summary
  merge_summary = tf.merge_summary
  SummaryWriter = tf.train.SummaryWriter
except:
  image_summary = tf.summary.image
  scalar_summary = tf.summary.scalar
  histogram_summary = tf.summary.histogram
  merge_summary = tf.summary.merge
  SummaryWriter = tf.summary.FileWriter

class batch_norm(object):
  def __init__(self, epsilon=1e-5, momentum = 0.9, name="batch_norm"):
    with tf.variable_scope(name):
      self.epsilon  = epsilon
      self.momentum = momentum
      self.name = name

  def __call__(self, x, train=True):
    return tf.contrib.layers.batch_norm(x,
                      decay=self.momentum, 
                      updates_collections=None,
                      epsilon=self.epsilon,
                      scale=True,
                      is_training=train,
                      scope=self.name)

# tf.random_normal_initializer
# tf.truncated_normal_initializer
def conv2d(input_, output_dim, 
       k_h=5, k_w=5, d_h=1, d_w=1, stddev=0.01,
       name="conv2d"):
  with tf.variable_scope(name):
    w = tf.get_variable('w', [k_h, k_w, input_.get_shape()[-1], output_dim],
              initializer=tf.random_normal_initializer(stddev=stddev))
    conv = tf.nn.conv2d(input_, w, strides=[1, d_h, d_w, 1], padding='SAME')
    #biases = tf.get_variable('biases', [output_dim], initializer=tf.constant_initializer(0.0))
    biases = tf.get_variable('biases', [output_dim], initializer=tf.random_uniform_initializer())
    conv = tf.reshape(tf.nn.bias_add(conv, biases), [-1, conv.get_shape()[1], conv.get_shape()[2], conv.get_shape()[3]])
    #conv = tf.reshape(tf.nn.bias_add(conv, biases), conv.get_shape())
    return conv

def lrelu(x, leak=0.2, name="lrelu"):
  return tf.maximum(x, leak*x)

def linear(input_, output_size, stddev=0.01,
           bias_start=0.0, name="Linear",with_w=False):
  with tf.variable_scope(name):
    shape = input_.get_shape().as_list()
    matrix = tf.get_variable("Matrix", [shape[1], output_size], tf.float32,
                              tf.random_normal_initializer(stddev=stddev))
    # bias = tf.get_variable("bias", [output_size],initializer=tf.constant_initializer(bias_start))
    bias = tf.get_variable('bias', [output_size], initializer=tf.random_uniform_initializer())
    if with_w:
      return tf.matmul(input_, matrix) + bias, matrix, bias
    else:
      return tf.matmul(input_, matrix) + bias

def max_pool(bottom,name):
  return tf.nn.max_pool(bottom, ksize=[1, 3, 3, 1], strides=[1, 2, 2, 1], padding='VALID', name=name)

def avg_pool(bottom,name):
  return tf.nn.avg_pool(bottom, ksize=[1, 3, 3, 1], strides=[1, 2, 2, 1], padding='VALID', name=name)

def sliceop(input,slicenum,outbit,name="slice"):
  with tf.variable_scope(name):
    batchsize=input.shape[0]
    slicesize=input.shape[1]/slicenum
    bn0 = batch_norm(name='bn0')
    #slices=bn0(linear(tf.slice(input,[0,0],[batchsize,slicesize]),outbit,name='linear0'))
    slices = bn0(linear(tf.slice(input, [0, 0], [-1, slicesize]), outbit, name='linear0'))
    print slices
    for i in range(1,slicenum):
      newstart=tf.cast((slicesize*i),tf.int32)
      bnx=batch_norm(name='bn'+str(i))
      slicex=bnx(linear(tf.slice(input,[0,newstart],[-1,slicesize]),outbit,name='linear'+str(i)))
      print slicex
      slices=tf.concat([slices,slicex],1)
    return slices


