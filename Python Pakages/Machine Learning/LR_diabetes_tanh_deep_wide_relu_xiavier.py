import tensorflow as tf
import numpy as np
import random
tf.set_random_seed(777)  # for reproducibility

#sigmoid 함수 보다 조금더 step function에 가까운 tanh으로 만든 sigmoid함수 적용.
def tanh_sigmoid(x):
    return (1/2)*(tf.tanh(x)+1)


####################################
# dropout (keep_prob) rate  0.7 on training, but should be 1 for testing
keep_prob = tf.placeholder(tf.float32)
####################################

xy = np.loadtxt('data_set/data-03-diabetes.csv', delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]     #훈련 데이터 범위 지정.
y_data = xy[:, [-1]]     #결과 라벨링 데이터 범위 지정.

print(x_data.shape, y_data.shape)

# placeholders for a tensor that will be always fed.
X = tf.placeholder(tf.float32, shape=[None, 8])   #데이터 크기에 따라 바꾸기.
Y = tf.placeholder(tf.float32, shape=[None, 1])

#########layer##########################################################

with tf.name_scope("Layer1"):  #name_scope를 활용하면 게층별로 깔끔한 정리가 가능. later1이라는 이름으로 아래 층을 정리.
    #W1 = tf.Variable(tf.random_normal([8, 10]), name='weight')   #데이터 크기에 따라 바꾸기.
    W1=tf.get_variable("W1", shape=[8, 10], initializer=tf.contrib.layers.xavier_initializer())
    b1 = tf.Variable(tf.random_normal([10]), name='bias')
    layer1 = tanh_sigmoid(tf.matmul(X, W1) + b1)
    #layer1 = tf.sigmoid(tf.matmul(X, W1) + b1)
    #layer1 = tf.nn.relu(tf.matmul(X, W1) + b1)
    layer1= tf.nn.dropout(layer1, keep_prob=keep_prob) ####################################
# 깊게 레이어가 쌓여지면 오버피팅이 발생함. 그래서 dropout은 오버피팅을 막기위하여 랜덤하게 부분부분만 사용해서 훈련시키는거.

    tf.summary.histogram("W1", W1)  #어떤 텐서를 로깅할 것인지 정하기.
    tf.summary.histogram("b1", b1)
    tf.summary.histogram("Layer1", layer1)


with tf.name_scope("Layer2"):  #name_scope를 활용하면 게층별로 깔끔한 정리가 가능. later1이라는 이름으로 아래 층을 정리.
    #W2 = tf.Variable(tf.random_normal([10, 10]), name='weight')   #데이터 크기에 따라 바꾸기.
    W2 = tf.get_variable("W2", shape=[10, 10], initializer=tf.contrib.layers.xavier_initializer())
    b2 = tf.Variable(tf.random_normal([10]), name='bias')
    layer2 = tanh_sigmoid(tf.matmul(layer1, W2) + b2)
    #layer2 = tf.sigmoid(tf.matmul(layer1, W2) + b2)
    #layer2 = tf.nn.relu(tf.matmul(layer1, W2) + b2)
    layer2 = tf.nn.dropout(layer2, keep_prob=keep_prob)  ####################################

    tf.summary.histogram("W2", W2)  #어떤 텐서를 로깅할 것인지 정하기.
    tf.summary.histogram("b2", b2)
    tf.summary.histogram("Layer2", layer2)

with tf.name_scope("Layer3"):  #name_scope를 활용하면 게층별로 깔끔한 정리가 가능. later1이라는 이름으로 아래 층을 정리.
    #W3 = tf.Variable(tf.random_normal([10, 1]), name='weight')   #데이터 크기에 따라 바꾸기.
    W3 = tf.get_variable("W3", shape=[10, 1],
                         initializer=tf.contrib.layers.xavier_initializer())
    b3 = tf.Variable(tf.random_normal([1]), name='bias')
    #hypothesis = tanh_sigmoid(tf.matmul(layer4, W5) + b5)
    hypothesis = tf.sigmoid(tf.matmul(layer2, W3) + b3)

    tf.summary.histogram("W3", W3)  # 어떤 텐서를 로깅할 것인지 정하기.
    tf.summary.histogram("b3", b3)
    tf.summary.histogram("Hypothesis", hypothesis)

########################################################################


# cost/loss function
with tf.name_scope("Cost"):
    cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))
    tf.summary.scalar("Cost", cost)   #summary하려는 값이 스칼라면 tf.summary.scalar를 사용

with tf.name_scope("Train"):
    #train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)
    train = tf.train.AdamOptimizer(learning_rate=0.01).minimize(cost)
'''
여러가지 optimizer들이 있다. 이 중에 현재 Adam이 제일 성능이 좋은 것으로 알려져있다. 
'''

# Accuracy computation
# True if hypothesis>0.5 else False
predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

# Launch graph
with tf.Session() as sess:
    # tensorboard --logdir=./logs/diabetes_tanh_deep_wide_logs_01
    merged_summary = tf.summary.merge_all()  # 모든 Summary들을 합쳐준다.
    writer = tf.summary.FileWriter("./logs/diabetes_tanh_deep_wide_logs_01")  # summary를 어디 위치에 파일로 만들어 놓을지 정하기.
    writer.add_graph(sess.graph)  # Show the graph  #그 파일에 그래프 좀 넣어줘.

    # Initialize TensorFlow variables
    sess.run(tf.global_variables_initializer())

    for step in range(10001):
        cost_val, _ = sess.run([cost, train], feed_dict={X: x_data, Y: y_data, keep_prob: 0.7})
        if step % 200 == 0:
            print(step, cost_val)

    # Accuracy report
    h, c, a = sess.run([hypothesis, predicted, accuracy],
                       feed_dict={X: x_data, Y: y_data, keep_prob: 1})
    print("\nHypothesis: ", h, "\nCorrect (Y): ", c, "\nAccuracy: ", a)






'''
0 0.82794
200 0.755181
400 0.726355
600 0.705179
800 0.686631
...
9600 0.492056
9800 0.491396
10000 0.490767

...

 [ 1.]
 [ 1.]
 [ 1.]]
Accuracy:  0.762846
'''

'''
tanh_sigmoid 함수 도입하니
Accuracy:  0.77338606
로 정확도 1%상승.
Hypothesis의 중요성.
'''

'''
2층 neural + tanh_sigmoid
Accuracy:  0.76679844
기존에서 0.1%상승.
'''

'''
5층 neural + tanh_sigmoid
Accuracy:  0.7720685
기존에서 1%상승.
'''

'''
5층 neural + sigmoid
Accuracy:  0.7220026
기존에서 -4% 하락.   아마 오버피팅이 문제인듯.
'''

