
'''
import calcpkg.operation
import calcpkg.geometry

print(calcpkg.operation.add(10,20))
print(calcpkg.operation.mul(10,20))

print(calcpkg.geometry.triangle_area(10,20))
print(calcpkg.geometry.rectangle_area(10,20))
'''

import calcpkg

print(calcpkg.operation.add(10,20))
print(calcpkg.operation.mul(10,20))

print(calcpkg.geometry.triangle_area(10,20))
print(calcpkg.geometry.rectangle_area(10,20))

from calcpkg import *

print(add(10,20))