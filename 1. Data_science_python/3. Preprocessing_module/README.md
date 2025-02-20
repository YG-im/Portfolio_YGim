# 데이터 탐색, 전처리 모듈

## preprocessing_module.py
  - 자세한 구현 예시 : [Examples] Genetic_algorithm_module and preprocessing_module.ipynb
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

## Genetic_algorithm_module.py 
  - 자세한 구현 예시 : [Examples] Genetic_algorithm_module and preprocessing_module.ipynb
  - 특징 선택 작업 중 가장 효율적인 작업인 유전 알고리즘을 수행할 수 있는 모듈
  - Deap이라는 진화알고리즘을 포함하는 모듈패키지가 있지만 사용을 위해 모듈을 파악하기가 어렵게 되어서 활용이 어려움. 이를 개선하기 위하여 유전알고리즘의 기본 원리를 바탕으로 활용이 쉬운 커스터마이징 모듈 제작.
  - 'from Genetic_algorithm import genetic_algorithm'하셔서 사용하시면 됩니다.
  - genetic_algorithm 함수 하나만 사용하면 도메인 지식 없이도 가장 최적의 특징선택을 진행 할 수 있습니다.
  
## Extract_inf_module.py  
  - 자세한 구현 예시 : [Example] Extract_inf_module.ipynb
  - 텍스트 데이터로 부터 전화번호, 이메일, 주민등록번호를 추출해주는 모듈로 아래와 같은 함수를 가지고 있음.
      - 숫자와 한글이 얽혀있는 전화번호를 깔끔하게 숫자로만 추출해주는 함수.
      - 텍스트들 중 이메일 주소만들 추출해주는 함수.
      - 텍스트들 중 주민등록번호를 추출해주고, 개인 정보보호를 위해 뒤에 6자리를 \*로 변환해주는 함수.
  
  
## [Examples] Genetic_algorithm_module and preprocessing_module.ipynb
  - Genetic_algorithm_module과 preprocessing_module 모듈의 자세한 사용예시입니다.
  - 이외의 자세한 함수 내 변수의 의미 혹은 사용법은 shift+tab을 사용하면 확인가능합니다.
  
## [Example] Extract_inf_module.ipynb
  -  Extract_inf_module 모듈의 자세한 사용예시입니다.
