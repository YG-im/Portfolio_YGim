# starGAN 논문 구현
- 'starGAN.ipynb'
    - starGAN을 tensorflow2.0으로 구현한 프로토타입 코드입니다.
    - GPU 환경이 구축되어있지 않아서 실제 training까지는 하지 못했습니다. 저자들은 training에 single NVIDIA Tesla M40 GPU로 하루가 소요되었다고 밝혔습니다. ("Training takes about one day on a single NVIDIA Tesla M40 GPU.")
    - 코드 내 데이터 셋은 논문에서 사용한 이미지 데이터 셋의 shape와 특성을 동일하도록 랜덤 생성한 텐서 데이터 사용하였습니다.
- 'starGAN arxiv1711.09020.pdf'
    - starGAN 논문 아카이브 버젼입니다.
- '[study] DCGAN' 폴더 
    - starGAN 구현을 위한 사전 학습으로 convolution을 사용한 가장 기본적인 GAN 알고리즘은 DCGAN에 대해서 공부한 자료.
    - 코드는 오픈소스를 사용하여 공부하였고, 자료는 논문을 비롯한 다양한 인터넷 자료들을 활용.
