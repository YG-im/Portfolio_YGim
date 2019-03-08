
# coding: utf-8

# # kera 패키지로 MNIST 손글씨 데이터 분류 ML
# - MNIST 손글씨 데이터를 분류하는 머신러닝을 keras 패키지를 활용하여 규현한 프로그램입니다.

# In[25]:


# import pakages 
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import Adam 
from keras.utils import np_utils


# In[29]:


import numpy as np
import random as rd


# - MNIST 데이터 로드

# In[15]:


(X_train, y_train), (X_test, y_test) = mnist.load_data('MNIST_data')


# - 데이터 전처리 : 자료형 변환 및 정규화

# In[16]:


# 데이터 자료형 변환
X_train = X_train.reshape(60000, 784).astype('float32') #float32자료형으로 바꾸기
X_test  = X_test.reshape(10000, 784).astype('float')
# 데이터 정규화
X_train /= 255
X_test  /= 255

# 라벨 데이터 재배열 : 0~9까지의 10개의 카테고리
y_train = np_utils.to_categorical(y_train, 10)
y_test  = np_utils.to_categorical(y_test, 10)


# - keras로 머신러닝 모델 구조 정의

# In[17]:


# 모델 구조 정의
model = Sequential()
# 1층
model.add(Dense(512, input_shape=(784,))) #28*28=784 열
model.add(Activation('relu')) # 활성함수 = relu function
model.add(Dropout(0.2))  #ratio of drop out = 0.2
# 2층
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))
# 3층
model.add(Dense(10))
model.add(Activation('softmax')) #멀티 클래스이기때문에 마지막은 softmax로 활성화


# - 머신러닝 모델 컴파일

# In[18]:


# 모델 구축
model.compile(
    loss='categorical_crossentropy',
    optimizer=Adam(),  #optimizer는 Adam으로.
    metrics=['accuracy'])


# - 머신러닝 훈련 및 평가하기

# In[20]:


# 훈련
hist = model.fit(X_train, y_train, epochs=2)

# 평가
score = model.evaluate(X_test, y_test, verbose=1)
print('loss=', score[0])
print('accuracy=', score[1])


# In[51]:


# test set에서 임의로 하나 뽑아서 예측해보기
rd_num = rd.randint(0, np.shape(X_test)[0] - 1) # test set에서 임의로 하나 추출
pred = model.predict(np.array([X_test[rd_num]]))
np.argmax(pred)


# In[57]:


# 결과 확인
np.argmax(y_test[rd_num])

