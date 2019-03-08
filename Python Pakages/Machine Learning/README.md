# Machine Learnig

- 'Classifier for MNIS data set only np and plt' 폴더
  - Tensorflow(tf)가 워낙 잘 구축되어있어서 tf의 함수들을 그냥 가져다가 쓰면 되지만, 심도있는 머신러닝 공부를 위해서는 tf의 내부구조를 파악해야합니다.
  - tf의 함수들은 Numpy(np)로 구현됩니다. tf에서 사용되는 주요 함수들과 backpropagation을 np로 구현하여 tf를 직접 구현해본 패키지입니다.

- 'data set', 'MNIST_data' 폴더
 - 아래 머신러닝에 사용된 데이터 셋이 들어있습니다.

- 머신러닝 설명 : 
  - tf_MNIST_classifier.py
    - tensorflow 패키지로 MNIST 손글씨 데이터 분류 ML
    - MNIST 손글씨 데이터를 분류하는 머신러닝을 tensorflow 패키지를 활용하여 규현한 프로그램입니다.
    - learning rate = 0.01, batch size = 100, drop out = 1 (단층 레이어이기때문.)
  - tf_LR_diabetes_sigmoid_tanh_relu_deep_wide_xiavier.py  
    - tf 패키지를 활용하여 당뇨를 예측하는 ML
    - 'data_set/diabetes.csv'에 있는 당뇨 정보를 훈련시킵니다.
    - 8가지의 판단 변수를 통해 예측을 합니다.
  - tf_animals_classifier_softmax.py
    - tf 패키지를 활용하여 특징으로부터 동물의 종을 알아내는 ML
    - 'data_set/animals.csv'를 통해 동물의 특징에 따른 종이 무엇인지 훈련합니다.
    - 주어진 동물의 특징에 따른 동물의 종을 알아맞출 수 있습니다.
  - keras_MNIST_classifier.py
    - kera 패키지로 MNIST 손글씨 데이터 분류 ML
    - MNIST 손글씨 데이터를 분류하는 머신러닝을 keras 패키지를 활용하여 규현한 프로그램입니다.
  - keras_BMI_test.py
    - Keras를 활용한 BMI test ML
    - keras 패키지를 이용하여 BMI를 판단하는 머신러닝입니다.
    - 'data_set/bmi.csv'에 있는 BMI 정보로 훈련을 시킵니다.
    - 몸무게(weight)와 키(height)를 입력하면 마름(thin), 정상(normal), 뚱뚱함(fat)을 판단해줍니다.

  
