# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import pickle
from dataset.mnist import load_mnist    #dataset 폴더에서 mnist.py에서 load_mnist 함수 가져오기
from functions import sigmoid, softmax  #함수들 모음에서 함수 가져오기


def get_data():      #load_mnist 함수가 MNIST 데이터에서 테스트 이미지들을 읽어오는 역할을 한다.
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network


def predict(network, x):                                      #predict함수는 각 레이블의 확률을 넘파이 배열로 반환한다.
    W1, W2, W3 = network['W1'], network['W2'], network['W3']  #예를 들어, [0.1,0.3,0.2,...,0.04]로 반환되면,
    b1, b2, b3 = network['b1'], network['b2'], network['b3']  #이미지를 예측한 숫자가 '0'일 확률이 0.1. '1'일 확률이 0.3임을 의미한다.

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y


x, t = get_data()
network = init_network()
accuracy_cnt = 0
for i in range(len(x)):
    y = predict(network, x[i])
    p= np.argmax(y) # predict로 반환된 [0.1,0.3,0.2,...,0.04] 중 가장 확률이 가장 높은 원소의 인덱스를 얻는다.
    if p == t[i]:
        accuracy_cnt += 1  #accuracy_cnt = 0에서 시작해서 신경망이 예측한 답변과 정답 레이블을 비교하여 맞힌 숫자를 센다.

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))   #신경망의 예측이 맞힌 총 답변의 갯수를 전체이미지 숫자로 나눠주어 정확도를 구한다.