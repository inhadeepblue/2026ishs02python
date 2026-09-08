import numpy as np

# numpy 배열 생성
array01 = np.array([3, 2, 1])
array02 = np.zeros((2, 3))
array03 = np.ones((3, 2))
array04 = np.arange(1, 11, 2)
# array04 = np.arange(5)
array05 = np.linspace(0, 1, 5)

print(array01)
print(array02)
array02[1, 1] = 9.0
print(array02)
print(array03)
print(array04)
print(array05)