# Tensorflow 추출하기
import tensorflow as tf

# 상수 정의
a = tf.constant(1234)
b = tf.constant(5000)

# 계산 정의
add_op = a + b

# 세션 시작하기
sess = tf.Session()
res = sess.run(add_op)
print(res)

###########################
import tensorflow as tf

# 상수 정의하기
a = tf.constant(2)
b = tf.constant(3)
c = tf.constant(4)

# 연산 정의하기
calc1_op = a + b * c
calc2_op = (a + b) * c

# 세션 시작하기
sess = tf.Session()
res1 = sess.run(calc1_op)
print(res1)
res2 = sess.run(calc2_op)
print(res2)
