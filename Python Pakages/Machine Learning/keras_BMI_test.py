
# coding: utf-8

# # Keras를 활용한 BMI test ML
# - keras 패키지를 이용하여 BMI를 판단하는 머신러닝입니다.
# - 'data_set/bmi.csv'에 있는 BMI 정보로 훈련을 시킵니다.
# - 몸무게(weight)와 키(height)를 입력하면 마름(thin), 정상(normal), 뚱뚱함(fat)을 판단해줍니다.

# In[2]:


#keras 패키지 import
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.callbacks import EarlyStopping
# pandas와 numpy 
import pandas as pd, numpy as np


# ### 1. 머신을 돌리기전에 **데이터를 전처리**해야한다.

# In[26]:


#데이터 불러들이기
csv = pd.read_csv("data_set/bmi.csv")


#    - 변수(input)에 해당하는 몸무게와 키 데이터를 전처리해준다.

# In[8]:


# 몸무게와 키 데이터 정규화
csv["weight"] /= 100 #csv에서 'weight'열 추출해서 예상 최대치인 100kg으로 정규화
csv["height"] /= 200 #csv에서 'height'열 추출해서 예상 최대치인 200kg으로 정규화

# 정규화된 몸무게와 키 데이터를 Nx2행렬로 만들기
X = csv[["weight", "height"]].as_matrix()
'''csv[["weight", "height"]]는 아래와 같이 나오기때문에 이 중 "weight", "height"만 추출해서 메트릭스 형태로 만들기.
       weight  height
0        0.62   0.710
1        0.73   0.710
2        0.61   0.885
3        0.48   0.935
4        0.60   0.765
....'''


# - 레이블(output)을 전처리해준다.
#     - thin, normal, fat으로 한글로 되어있는 데이터를 0,1로 나타내주어야한다.
#     - 세 개의 클래스이니 각각 1열 3행 텐서로 변화시켜준다.

# In[18]:


# 라벨(y) 전처리
bmi_class = {"thin":[1,0,0], "normal":[0,1,0], "fat":[0,0,1]} # BMI 클래스들을 텐서로 설정
y = np.empty((20000,3)) #2000x3로 된 0 행렬을 만들어서 20000개의 각 데이터의 라벨을 넣을 빈 셋을 만든다.

for idx, label in enumerate(csv["label"]): # 하나씩 y행렬에 넣어준다.
    y[idx] = bmi_class[label]


# - 훈련데이터와 테스트 데이터로 나누기

# In[27]:


#총 20000개의 데이터중 15000개는 훈련데이터로 나머지 5000개는 테스트 데이터로 만든다
X_train, y_train = X[1:15001], y[1:15001]
X_test,  y_test  = X[15001:20001], y[15001:20001] 


# ### 2. 머신러닝 모델을 정의 및 구축

# - keras 패키지를 활용하여 모델을 정의한다.

# In[28]:


# Sequential() class를 객체화해서 model 만들 준비를 한다.
model = Sequential()
# 1층
model.add(Dense(512, input_shape=(2,)))
model.add(Activation('relu')) # 활성함수 : relu function
model.add(Dropout(0.1))   #ratio of drop out = 0.1
# 2층
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.1))
# 3층
model.add(Dense(3))
model.add(Activation('softmax'))  #다층 클래스이기 때문에 마지막엔 softmax함수로 활성화.


# - 모델을 컴파일한다. 

# In[31]:


# 모델 구축
model.compile(
    loss='categorical_crossentropy', # cost 함수를 cross entropy로 정의한다.
    optimizer="rmsprop",             # optimizer를 선택한다.
    metrics=['accuracy'])


# ### 3. 데이터 훈련 및 평가

# - 훈련데이터를 이용하여 머신을 훈련시킨다.

# In[34]:


# 데이터 훈련
hist = model.fit(
    X_train, y_train,
    batch_size=100,
    epochs=20,
    validation_split=0.1,
    callbacks=[EarlyStopping(monitor='val_loss', patience=2)],
    verbose=1)


# - 테스트 데이터로 머신러닝 테스트

# In[35]:


# 평가
score = model.evaluate(X_test, y_test)
print('loss=', score[0])
print('accuracy=', score[1])


# # 훈련 머신으로 사용자의 BMI를 측정해주는 프로그램

# In[73]:


# 몸무게와 키를 입력받기
weight_new = int(input("몸무게(kg)를 넣어주세요. : "))
height_new = int(input("키(cm)를 넣어주세요. : "))

# 훈련된 머신으로 예측
pred = model.predict(np.array([[weight_new/100 , height_new/200]])) #array로 바꿔주는게 중요!!
pred_argmax = np.argmax(pred)

# 결과 출력.
if pred_argmax == np.argmax(bmi_class['thin']):
    print('BMI 결과 마른 체형이 나왔습니다. 많이 드시고 운동하시길 바랍니다!')
elif pred_argmax == np.argmax(bmi_class['normal']):
    print('BMI 결과 정상 체형이 나왔습니다. 이 상태를 유지하세요!')
elif pred_argmax == np.argmax(bmi_class['fat']):
    print('BMI 결과 뚱뚱한 체형이 나왔습니다. 다이어트를 하셔야겠어요!')
else:
    print('에러가 났습니다. 다시 입력해주세요.')

