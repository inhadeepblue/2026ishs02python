import numpy as np

array01 = np.zeros((3, 4))

# print(array01)
# print(array01.ndim)
# print(array01.size)
array01[2, 1] = 7.0
array01[1, 2] = 11.0
print(array01)
print(array01[1:, [1]])
print(array01[1:, [1, 2]])
print(array01[1:, 1:3])
print(array01[array01 <= 7])