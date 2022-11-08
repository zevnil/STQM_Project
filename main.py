from validData import *
import tensorflow as tf

# valid_prs, dev, rev = validData()
temp = [[1, 2, 3], [4, 5, 6]]
temp1 = [[7, 8, 9], [10, 11, 12]]
temp2 = tf.convert_to_tensor(temp)
temp3 = tf.convert_to_tensor(temp1)
temp4 = tf.stack([temp2, temp3], axis = 0)
# print(temp2)
print(temp4)