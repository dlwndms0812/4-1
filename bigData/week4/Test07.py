#Test07 : numpy 실습

import numpy as np

ar1 = np.array([1, 2, 3, 4, 5])
print(ar1)
print()

print(type(ar1))
print()


ar2 = np.array([[10, 20, 30], [40, 50, 60]])
print(ar2)
print()

ar3 = np.arange(1, 11, 2)
print(ar3)
print()

ar4 = np.array([1, 2, 3, 4, 5, 6]).reshape((3, 2)) #reshape는 해당 행, 열로 재표현
print(ar4)
print()

ar5 = np.zeros((2, 3)) #생성과 동시에 초기화
print(ar5)
print()

ar6 = ar2[0:2, 0:2] #행과 열의 범위를 지정
print(ar6)
print()

ar7 = ar1 + 10
print(ar7)
print()

print(ar1 + ar7)
print()

print(ar7 - ar1)
print()

print(ar1 * 2)
print()

print(ar1 / 2)
print()

ar8 = np.dot(ar2, ar4) #행렬 곱
print(ar8)
print()