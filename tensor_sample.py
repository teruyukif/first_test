import numpy as np
import tensorflow as tf

w = tf.Variable(tf.zeros([2, 1]))
b = tf.Variable(tf.zeros([1]))

x = tf.placeholder(tf.float32, shape=[None, 2])
t = tf.placeholder(tf.float32, shape=[None, 1])
y = tf.nn.sigmoid(tf.matmul(x, w) + b)

#交差エントロピー誤差関数
cross_entropy = - tf.reduce_sum(t * tf.log(y) + (1 - t) * tf.log(1 - y))

＃勾配降下法
train_step = tf.train.GradientDescentOptimizer (0.1).minimize(cross_entropy)



#print(w)
