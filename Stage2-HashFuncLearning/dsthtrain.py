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
from dsthmodelv2 import *

class Train(object):
    def __init__(self,sess):
        self.sess=sess

    def train(self,model,config):
        n_optim=tf.train.GradientDescentOptimizer(config.learning_rate).minimize(model.loss, var_list=model.t_vars)
        #n_optim = tf.train.AdamOptimizer(config.learning_rate, beta1=config.beta1).minimize(model.loss, var_list=model.t_vars)
        nconv1_w = [var for var in model.t_vars if 'n_conv1/biases' in var.name]
        bn3_beta = [var for var in model.t_vars if 'bn3/beta' in var.name]
        nslice_bn2_beta=[var for var in model.t_vars if 'n_slice/bn2/beta' in var.name]
        try:
            tf.global_variables_initializer().run()
        except:
            tf.initialize_all_variables().run()

        self.writer = SummaryWriter("../logs", self.sess.graph)
        self.n_sum = merge_summary([model.loss_sum])
        counter = 1
        start_time = time.time()
        could_load, checkpoint_counter = model.load(self,model.checkpoint_dir)
        if could_load:
            counter = checkpoint_counter
            print(" [*] Load SUCCESS")
        else:
            print(" [!] Load failed...")

        ids,datas,self.data=getidsAndimages(config.dataset_name)
        self.hashtags=getHashtags(config.dataset_name).astype(np.int32)

        batch_idxs = min(len(ids), config.train_size) // config.batch_size
        for epoch in xrange(config.epoch):
            for idx in xrange(0, batch_idxs):
                batch1 = self.data[idx * config.batch_size:(idx + 1) * config.batch_size]
                batch_images = np.array(batch1).astype(np.float32)
                batch2=self.hashtags[idx * config.batch_size:(idx + 1) * config.batch_size]
                batch_hashtags=np.array(batch2).astype(np.float32)
                _, summary_str=self.sess.run([n_optim,self.n_sum],
                                             feed_dict={model.inputs:batch_images,
                                                        model.hashtags:batch_hashtags})
                self.writer.add_summary(summary_str, counter)
                logits=model.logits.eval({model.inputs:batch_images,
                                          model.hashtags:batch_hashtags})
                err=model.loss.eval({model.inputs:batch_images,
                                     model.hashtags:batch_hashtags})
                accracy=model.accuracy.eval({model.inputs:batch_images,
                                             model.hashtags:batch_hashtags})
                counter += 1
                print("Epoch: [%2d] [%4d/%4d] time: %4.4f, loss: %.8f, accracy:%8f" \
                      % (epoch, idx, batch_idxs,time.time() - start_time, err,accracy))
                print "logit:"
                print logits
                print "hashtags"
                print batch_hashtags
                '''print("nconv1_w",self.sess.run(nconv1_w))
                print("bn3_beta", self.sess.run(bn3_beta))
                print("nslice_bn2_beta", self.sess.run(nslice_bn2_beta))'''
                if np.mod(counter, 500) == 2:
                    model.save(self,config.checkpoint_dir, counter)
