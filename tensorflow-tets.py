import tensorflow as tf

tf.enable_eager_execution()

print(tf.executing_eagerly())

x = [[2.]]
m = tf.matmul(x, x)
print("hello, {}".format(m))
 
