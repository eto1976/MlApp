#! /usr/bin/python
# coding:utf-8
#
#   tf_sample_square_error.py
#
#                   Jun/05/2017
# ------------------------------------------------------------------
import sys
import tensorflow as tf

sys.stderr.write("*** start ***\n")

input_x = [[1.],[5.]]
input_y = [[4.],[2.]]

x = tf.placeholder("float", [None, 1])
y_ = tf.placeholder("float", [None, 1])

a = tf.Variable([1.], name="slope")
b = tf.Variable([0.], name="y-intercept")
y = tf.multiply(a, x) + b

init = tf.global_variables_initializer()

# 誤差関数
loss = tf.reduce_sum(tf.square(y_ - y))

# トレーニング方法は、勾配降下法を選択
train_step = tf.train.GradientDescentOptimizer(0.03).minimize(loss)


with tf.Session() as sess:
    sess.run(init)
    print('初期状態')
    print('誤差' + str(sess.run(loss, feed_dict={x: input_x, y_: input_y})))
    print("slope: %f, y-intercept: %f" % (sess.run(a), sess.run(b)))

    for step in range(100):
        sess.run(train_step, feed_dict={x: input_x, y_: input_y})
        if (step+1) % 20 == 0:
            print('\nStep: %s' % (step+1))
            print('誤差' + str(sess.run(loss, feed_dict={x: input_x, y_: input_y})))
            print("slope: %f, y-intercept: %f" % (sess.run(a), sess.run(b)))
#
sys.stderr.write("*** end ***\n")
# ------------------------------------------------------------------