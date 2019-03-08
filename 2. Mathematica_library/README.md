# Mathematica
Mathematica code for research
- 연구자들을 위하여 만든 Mathematica 라이브러리 입니다.
  - \*\*\*.nb는 Mathematica 확장자입니다.
  - Mathematica는 파워풀한 심볼릭 계산과 수학과 연계한 직관적 코드를 작성할 수 있다는 강점이 있습니다.
  - 하지만 계산이 무거워질 수록 계산에 요구되는 컴퓨터 성능이 지수적으로 커진다는 단점이 있습니다.
  - 따라서 무거운 수치 시뮬레이션은 파이썬 프로그램을 참고하시기 바랍니다.

- 패키지 설명
  - Solution to PDE Pakage.nb 
    - 고차원 편미분 방정식을 효율적으로 풀기위해 만들어진 패키지입니다. 
    - Newtonian method를 활용하여 해를 찾는 것을 기본으로 하고 있습니다. 
    - 패키지 내부 예시는 모델에따른 effective potential에 대한 편미분 방정식을 풀어서 spectral gap을 계산하는 예시입니다. 
    - 이를 시각화하는 다양한 방법도 제시되어있으니 참고하시기 바랍니다.
  - WKB Numerical Simulation Pakage.nb 
    - 수학 방법론에서 가장 많이 쓰이는 WKB 근사를 위한 패키지입니다. 
    - 패키지에는 Newtonian method를 통하여 effective potential의 극소지점을 찾은 후 그를 기준으로 WKB근사를 하는 예시가 담겨있습니다. 
    - 이를 시각화하는 다양한 방법도 제시되어있습니다.
  - Tensor calculation basic Pakage.nb 
    - N차원 tensor을 활용한 다양한 텐서 연산을 구현한 패키지입니다. 
    - 기본적인 미분 정의와 이를 활용하여 Riman curvature, Christoffel symbols 등을 계산할 수 있습니다.
  - Tensor Calculations Pakage by Sigma.nb 
    - Sigma 알고리즘을 활용하여 텐서 연산을 구현했습니다. 
    - 'Tensor calculation basic Pakage.nb'의 코드들을 활용하여 복잡한 물리계에서 실제 의미를 가지는 물리량을 추출해내는 패키지입니다. 
    - Quasi-local conserved charge, Wald entory 등을 계산할 수 있습니다.
  - Tensor Calculations Pakage by X-tensor.nb 
    - X-tensor을 활용하여 구현한 텐서 패키지입니다. 
    - 구현한 텐서연산은 ' Tensor Calculations Pakage by Sigma.nb'와 동일하지만 코드에대한 직관적인 이해가 더 용이한 패키지입니다. 
    - 다만, ' Tensor Calculations Pakage by Sigma.nb'에 비해 코드가 많이 무거워서 간단한 형태의 텐서에 대한 연산만 가능합니다.
