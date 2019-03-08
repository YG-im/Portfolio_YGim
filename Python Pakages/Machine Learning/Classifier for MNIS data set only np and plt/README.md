# Numpy와 Matplotlib으로 구현하는 머신러닝

- Tensorflow(tf)가 워낙 잘 구축되어있어서 tf의 함수들을 그냥 가져다가 쓰면 되지만, 심도있는 머신러닝 공부를 위해서는 tf의 내부구조를 파악해야합니다.
- tf의 함수들은 Numpy(np)로 구현됩니다. tf에서 사용되는 주요 함수들과 backpropagation을 np로 구현하여 tf를 직접 구현해본 패키지입니다.
- 패키지 설명 : 
  - functions.py
      - 머신러닝을 구현할 때 필요한 함수들을 np로 직접 구현한 패키지입니다.
      - 내장 함수 : sigmoid, identify_function, sigmoid_grad, relu, relu_grad, softmax, mean_squared_error, cross_entropy_error, softmax_loss
  - mnist_NN_with_sample_w.py
      - backward propagation을 구현하지 않고, 주어진 weight(sample_weight.pkl)를 활용하여 MNIST 데이터셋 분류기를 구현해본 것입니다.
  - 
