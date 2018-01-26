from __future__ import division
import os
import time
import math
from glob import glob
import tensorflow as tf
import numpy as np
from six.moves import xrange

from ops import *
from utils import *

class Model(object):
  def __init__(self, input_height=32, input_width=32,output_height=3,
               output_width=3,batch_size=64,f1_dim=32,f2_dim=32,
                f3_dim=64,f4_dim=64,f5_dim=128,f6_dim=128, fc_dim=4096,
               hashbit=48,slicenum=16,outbit=3,size=32,c_dim=3,
               dataset_name='default',checkpoint_dir="../checkpoint",crop=True):
    """
    Args:
      sess: TensorFlow session
      batch_size: The size of batch. Should be specified before training.
      f1_dim: (optional) Dimension of gen filters in first conv layer. [64]
      f2_dim: (optional) Dimension of discrim filters in first conv layer. [64]
      f3_dim: (optional) Dimension of gen filters in first conv layer. [64]
      f4_dim: (optional) Dimension of discrim filters in first conv layer. [64]
      f5_dim: (optional) Dimension of gen filters in first conv layer. [64]
      f6_dim: (optional) Dimension of discrim filters in first conv layer. [64]
      c_dim: (optional) Dimension of image color. For grayscale input, set to 1. [3]
    """
    self.batch_size = batch_size
    self.input_height = input_height
    self.input_width = input_width
    self.output_height = output_height
    self.output_width = output_width

    self.f1_dim = f1_dim
    self.f2_dim = f2_dim
    self.f3_dim = f3_dim
    self.f4_dim = f4_dim
    self.f5_dim = f5_dim
    self.f6_dim = f6_dim
    self.fc_dim = fc_dim
    self.c_dim=c_dim
    self.crop=crop

    self.bn3 = batch_norm(name='bn3')

    self.dataset_name = dataset_name
    self.checkpoint_dir = checkpoint_dir

    self.hashbit=hashbit
    self.slicenum=slicenum
    self.outbit=outbit
    self.size=size
    if self.dataset_name == 'cifar10':
        self.c_dim=3

    self.build_model()

  def build_model(self):
      if self.crop:
          image_dims = [self.output_height, self.output_width, self.c_dim]
      else:
          image_dims = [self.input_height, self.input_width, self.c_dim]

      # self.inputs = tf.placeholder(tf.float32, [self.batch_size] + image_dims, name='images')
      # self.hashtags = tf.placeholder(tf.float32, [self.batch_size, self.hashbit], name='hashbit')

      self.inputs = tf.placeholder(tf.float32, name='images',shape = [None]+image_dims)
      self.hashtags = tf.placeholder(tf.float32,name='hashbit',shape=[None, self.hashbit])

      inputs = self.inputs
      hashtags=self.hashtags

      self.logits=self.network(inputs,32)

      def sqrt_l2_loss_2(x,y):
          diff=tf.subtract(y,x)
          loss=tf.sqrt(tf.reduce_sum(tf.square(diff),1))
          return loss

      with tf.variable_scope('Loss'):
          self.loss=tf.reduce_mean(sqrt_l2_loss_2(self.logits,hashtags))

      self.loss_sum = scalar_summary("loss", self.loss)

      with tf.variable_scope('Accuracy'):
          abslogits=tf.abs(self.logits,name="abslogits")
          predictions = tf.cast(tf.greater(abslogits, 0.5),tf.int32,name="predictions")
          hashtags=tf.cast(hashtags,tf.int32)
          print predictions
          print hashtags
          correct_predictions = tf.equal(predictions, hashtags, name="correct_predictions")
          self.accuracy = tf.reduce_mean(tf.cast(correct_predictions, tf.float32))

      self.t_vars = tf.trainable_variables()
      # self.n_vars = [var for var in t_vars if 'n_' in var.name]
      # print self.n_vars
      self.saver = tf.train.Saver()

  def network(self,image,size):
      with tf.variable_scope("network"+str(size)) as scope:
          conv1=conv2d(image,self.f1_dim,name='n_conv1')
          pool1=max_pool(conv1,name='n_pool1')
          conv2=conv2d(pool1,self.f2_dim,name='n_conv2')
          pool2=avg_pool(conv2,name='n_pool2')
          conv3=tf.nn.relu(self.bn3(conv2d(pool2,self.f3_dim,name='n_conv3')),name='n_relu3')
          pool3=avg_pool(conv3,name='n_pool3')
          fc=linear(tf.reshape(pool3, [-1, 3*3*64]), 4096,name='n_fc')
          slices=sliceop(fc,self.slicenum,self.outbit,name='n_slice')
          return slices

  @property
  def model_dir(self):
      return "{}_{}_{}_{}".format(
          self.dataset_name, self.batch_size,
          self.output_height, self.output_width)

  def save(self, train, checkpoint_dir, step):
      model_name = "DSTH.model"
      checkpoint_dir = os.path.join(checkpoint_dir, self.model_dir)

      if not os.path.exists(checkpoint_dir):
          os.makedirs(checkpoint_dir)

      self.saver.save(train.sess,
                      os.path.join(checkpoint_dir, model_name),
                      global_step=step)

  def load(self, train, checkpoint_dir):
      import re
      print(" [*] Reading checkpoints...")
      checkpoint_dir = os.path.join(checkpoint_dir, self.model_dir)
      ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
      if ckpt and ckpt.model_checkpoint_path:
          ckpt_name = os.path.basename(ckpt.model_checkpoint_path)
          self.saver.restore(train.sess, os.path.join(checkpoint_dir, ckpt_name))
          counter = int(next(re.finditer("(\d+)(?!.*\d)", ckpt_name)).group(0))
          print(" [*] Success to read {}".format(ckpt_name))
          #print (train.sess.run(self.logits))
          return True, counter
      else:
          print(" [*] Failed to find a checkpoint")
          return False, 0
