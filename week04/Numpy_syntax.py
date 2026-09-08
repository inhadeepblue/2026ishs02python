import numpy as np

array01 = np.array([3, 2, 1])
array02 = np.zeros((2, 3))
array03 = np.ones((3, 2))
array04 = np.arange(1, 11, 2)
# array04 = np.arange(5)
array05 = np.linspace(0, 1, 5)

# 배열 속성
print(array01.shape)  # 배열 모양 (행, 열)
print(array02.shape)
print(array02.ndim)  # 차원 수
print(array03.dtype)  # 데이터 타입
print(array04.size)  # 전체 원소 개수
print(array05.size)