# 데이터 탐색, 전처리 모듈

## preprocessing_module.py (자세한 구현 예시 : Examples.ipynb)
  - 데이터 탐색과 전처리 때마다 매번 반복해서 하는 작업을 효율적으로 하고 전체 코드를 깔끔하게 작성하기 위하여 만든 모듈.
  - 특징들을 분류하고, 왜도를 탐색하고, 그래프를 그려보고, 상관관계를 구해보는 등 처음 데이터를 탐색할 때 수행하는 반복 작업들을 효율적으로 진행하기 위한 모듈입니다.
  - 반복적으로 사용하는 작업을 하나의 함수로 만들었기 때문에 코드를 복사해와서 데이터에 맞게 수정해서 다시 돌리는 작업을 함수 한줄로 사용가능합니다.
  - 'from preprocessing_module import *'하셔서 사용하시면 됩니다.
  - 모듈에 내장되어있는 함수의 종류
    - 'categ_or_contin' : categorical variable과 continuous variable을 자동으로 분류해주는 함수.
    - 'count_category' : categorical variable들 별로 category 종류와 각 category별 value의 갯수를 보여주는 함수.
    - 'corr_heatmap' : column들 간의 상관관계를 heatmap으로 보여주는 함수.
    - 'corr_btw_x_y_VS_fixed_col' : 각 category에 따른 특징 vs label의 상관관계 조사해주는 함수.
    - 'x_vs_y_with_fixed_col' : 각 category에 따른 특징 vs label의 그래프들를 보여주는 함수
    - 'features_Boxplot' : categorical variable을 Boxplot으로 분포를 보여주는 함수.
    - 'one_feature_vs_freqency' : 하나의 특징의 빈번도를 distplot으로 보여주는 함수.(왜도, 평균, 표준편차 출력)
    - 'features_vs_frequency' : 특징들의 빈번도를 distplot으로 보여주는 함수.(여러개를 동시에 행렬형태로 출력가능) 
    - 'features_vs_label' : 특징과 라벨의 그래프를 regplot으로 보여주는 함수.(여러개를 동시에 행렬형태로 출력가능)
    - 'rowXcol_for_subfig' : 여러 개의 그래프를 subfig의 행렬형태로 그릴때 가장 최적의 행렬 형태를 출력해주는 함수.    
    - 'test_for_transf' : 특징을 가공할때 원하는 변환 함수만 입력하면 특징의 분포변화를 보여주는 함수.
    - 'Remove_outliers' : 입력해준 기준에 부합하지 않는 이상치를 제거해주는 함수.
    - 'check_skew' : 특징들의 왜도를 체크해주고 입력한 기준에 미달되는 특징을 분류해주는 함수.
    - 'rmse' : root mean squared error

## Genetic_algorithm_module.py (자세한 구현 예시 : Examples.ipynb)
  - 특징 선택 작업 중 가장 효율적인 작업인 유전 알고리즘을 수행할 수 있는 모듈
  - 기존에 유전알고리즘이 구현되어있는 패키지가 있지만 맞춤형으로 간단하게 구현해본 코드입니다.
  - 'from Genetic_algorithm import genetic_algorithm'하셔서 사용하시면 됩니다.
  - genetic_algorithm 함수 하나만 사용하여 가장 최적의 특징선택을 하실 수 있습니다.
  
## Examples.ipynb
  - 위의 두 가지 모듈의 자세한 사용예시입니다.
  - 이외의 자세한 함수 내 변수의 의미 혹은 사용법은 shift+tab을 사용하면 확인가능합니다.
