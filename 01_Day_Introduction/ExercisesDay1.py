# 1.1 Check the python version you are using
import sys
print(sys.version)

""" 1.2 Open the python interactive shell and do the following operations. The operands are 3 and 4.
addition(+)
subtraction(-)
multiplication(*)
modulus(%)
division(/)
exponential(**)
floor division operator(//) """
print('3 + 4 : ', 3 + 4)
print('3 - 4 : ', 3 - 4)
print('3 * 4 : ', 3 * 4)
print('3 % 4 : ', 3 % 4)
print('3 / 4 : ', 3 / 4)
print('3 ** 4 : ', 3 ** 4)

# 1.3 Write strings on the python interactive shell. The strings are the following:
print('Cassiano')
print('Czz')
print('S. Solar,P. Terra, Bitcoin City')
print('I am enjoying 30 days of python')

# 1.4 Check the data types of the following data:
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print('Cassiano')
print('Czz')
print('S. Solar,P. Terra, Bitcoin City')

# 3.2 Find an Euclidian distance between (2, 3) and (10, 8)
# With numPy
import numpy
point_a = (2,3)
point_b = (10,8)
# Forma A
distancia_euclidiana_a =  numpy.linalg.norm(point_a-point_b)
print(distancia_euclidiana_a)

# Forma B
distancia_euclidiana_b =  numpy.sqrt(numpy.sum(numpy.square(point_a-point_b)))
print(distancia_euclidiana_b)

# Forma C
import math
distancia_euclidiana_c =  math.dist(point_b,point_b)
print(distancia_euclidiana_c)

# Forma D - Processamento mais rapido

from scipy.spatial import distance
distancia_euclidiana_d =  distance.euclidean(point_b,point_b)
print(distancia_euclidiana_d)






