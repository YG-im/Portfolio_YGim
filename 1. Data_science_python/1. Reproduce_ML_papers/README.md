# 머신러닝 논문구현 프로젝트
- 머신러닝 논문들 중 GAN에 대한 논문을 직접 구현하여 그 원리와 구현 방법에 대해 연구하는 프로젝트입니다.
- 사용 framework : tensorflow2.0
- cf) GPU 사용여건이 안되어 데이터 셋은 논문에서 사용한 이미지 데이터 셋의 shape와 특성을 동일하도록 랜덤 생성한 텐서 데이터 사용하였습니다.
1. 구현 완료 : Star GAN
    - 최근 가장 핫하게 떠오른 GAN 알고리즘 중 하나인 starGAN을 tensorflow2.0을 사용하여 구현.
      - title : StarGAN: Unified Generative Adversarial Networks for Multi-Domain Image-to-Image Translation (arXiv:1711.09020)
      - authors : Yunjey Choi, Minje Choi, Munyoung Kim, Jung-Woo Ha, Sunghun Kim, Jaegul Choo  
    - 'starGAN'폴더에는 GAN의 기본 알고리즘인 DCGAN을 오픈소스와 여러 자료들을 참고하여 공부하며 정리한 ipynb 코드도 들어있습니다.  
2. 구현 예정 : Wavenet 
    - title : WAVENET: A GENERATIVE MODEL FOR RAW AUDIO (arXiv:1609.03499)
    - authors : Aaron van den Oord, Sander Dieleman, Heiga Zen, Karen Simonyan, Oriol Vinyals, Alex Graves, Nal Kalchbrenner, Andrew Senior, Koray Kavukcuoglu
