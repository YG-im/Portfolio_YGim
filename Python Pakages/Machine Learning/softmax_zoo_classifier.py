# Lab 6 Softmax Classifier
import tensorflow as tf
import numpy as np
tf.set_random_seed(777)  # for reproducibility

# Predicting animal type based on various features
xy = np.loadtxt('data-04-zoo.csv', delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

print(x_data.shape, y_data.shape)

'''
(101, 16) (101, 1)
'''

nb_classes = 7  # 0 ~ 6, 7가지 종류의 동물로 분류한다.

X = tf.placeholder(tf.float32, [None, 16]) #기준이 되는 동물의 특징 갯수가 16가지
Y = tf.placeholder(tf.int32, [None, 1])  # 0 ~ 6, 아직 one hot이 아닌 데이터임.

Y_one_hot = tf.one_hot(Y, nb_classes)  # one hot
print("one_hot:", Y_one_hot)
Y_one_hot = tf.reshape(Y_one_hot, [-1, nb_classes])
print("reshape one_hot:", Y_one_hot)


'''
i) one_hot : 
one_hot으로 만든다는 것은 아래 같은것.
[[0],[3]]  : 2nd rank tensor, 2x1 matrix
-> Y_one_hot=[[[1,0,0,0,0,0,0]],[[0,0,0,1,0,0,0]]] : 3rd rank tensor, 2x1x7 matrix (새로운 axis가 추가됨)
ii) reshape :
reshape를 해서 필요없는 axis하나를 빼준다.
-> tf.reshape(Y_one_hot, [-1, nb_classes]) = [[1,0,0,0,0,0,0],[0,0,0,1,0,0,0]] 
: 2rd rank tensor, 2x7 matrix (새로운 axis가 제거됨)
'''

'''
one_hot: Tensor("one_hot:0", shape=(?, 1, 7), dtype=float32)
reshape one_hot: Tensor("Reshape:0", shape=(?, 7), dtype=float32)
'''

W = tf.Variable(tf.random_normal([16, nb_classes]), name='weight')
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')

# tf.nn.softmax computes softmax activations
# softmax = exp(logits) / reduce_sum(exp(logits), dim)
logits = tf.matmul(X, W) + b
hypothesis = tf.nn.softmax(logits)

# Cross entropy cost/loss
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits,
                                                                 labels=tf.stop_gradient([Y_one_hot])))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

#########################
prediction = tf.argmax(hypothesis, 1) #hypothesis의 열에서 가장 큰 값의 인텍스를 반환다.
correct_prediction = tf.equal(prediction, tf.argmax(Y_one_hot, 1)) #Y_one_hot 중에 큰거 하나 택한 값과, prediction이 같냐?
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32)) #그것들을 더해서 평균내서 확률로 바꾼다.
print("prediction:", prediction, "correct_prediction:", correct_prediction, "accuracy:", accuracy)
#########################
'''
tf.argmax(a, 0)는 2차원 배열의 각 열에서 가장 큰 값을 찾아 인덱스를 반환합니다.
tf.argmax(a, 1)는 2차원 배열의 각 행에서 가장 큰 값을 찾아  인덱스를 반환합니다.. 
MNIST 코드에서는 one hot 벡터로 표현한 라벨이 의미하는 숫자를 찾기 위해 tf.argmax 함수를 사용됩니다. 
예를 들어 다음처럼 10개의 숫자중 세번째 인덱스의 값이 1이라면 이 라벨은 숫자 2를 의미합니다. 
이때 세번째 인덱스가 가장 큰 값임을 빨리 찾기위해 tf.argmax 함수를 사용합니다.
[ 0 0 1 0 0 0 0 0 0 0]
라벨이 1차원 벡터인데 실제 코드에서 보면 tf.argmax 함수의 두번째 인자로 1을 사용하고 있습니다. 
이것은 pred와 y의 shape를 출력해보면 알 수 있습니다. (?, 10) 로 출력됩니다. 
첫번째 차원은 라벨의 갯수를 표현하기 위해 사용되므로 크기가 정해져 있지 않으며 두번째 차원은 0~9까지 10개의 숫자를 위한 라벨로 사용하기 때문에 10입니다.
두번째 차원을 라벨로 사용하기 때문에 0이 아닌 1을 사용하게 됩니다. 즉 각 행에서 최대값을 찾습니다. 
Ex) correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
'''


# Launch graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(2001):
        _, cost_val, acc_val = sess.run([optimizer, cost, accuracy], feed_dict={X: x_data, Y: y_data})
                                        
        if step % 100 == 0:
            print("Step: {:5}\tCost: {:.3f}\tAcc: {:.2%}".format(step, cost_val, acc_val))

    # Let's see if we can predict
    pred = sess.run(prediction, feed_dict={X: x_data})
    # y_data: (N,1) = flatten => (N, ) matches pred.shape
    for p, y in zip(pred, y_data.flatten()): #flatten : y=[[0],[2],...] -> y=[0,2,...]
                                            # zip : p,y로 넘기기 편하게 묵어준다.
        print("[{}] Prediction: {} True Y: {}".format(p == int(y), p, int(y)))




'''
Step:     0 Loss: 5.106 Acc: 37.62%
Step:   100 Loss: 0.800 Acc: 79.21%
Step:   200 Loss: 0.486 Acc: 88.12%
...
Step:  1800	Loss: 0.060	Acc: 100.00%
Step:  1900	Loss: 0.057	Acc: 100.00%
Step:  2000	Loss: 0.054	Acc: 100.00%
[True] Prediction: 0 True Y: 0
[True] Prediction: 0 True Y: 0
[True] Prediction: 3 True Y: 3
...
[True] Prediction: 0 True Y: 0
[True] Prediction: 6 True Y: 6
[True] Prediction: 1 True Y: 1
'''
