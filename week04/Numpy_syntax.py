import numpy as np

array01 = np.zeros((3, 4))
array02 = np.array([[1, 2, 3, 88], [-9, 4, 5, 6], [7, 55, 8, 9]])

array01[0, 0] = 7.0
print(array01)
#print(array01.reshape((2, 6)))
print(array02)
print(array01 + array02)
print(array01 + 4.1)
print(np.sum(array01))