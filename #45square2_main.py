'''
import square2

print(square2.base)
print(square2.square(10))

from square2 import base, square
print(base)
print(square(10))

import person

maria = person.Person('마리아', 20, '서울')
maria.greeting()

import hello
print('main.py __name__:', __name__)
'''

#calc.py
def add(a,b):
    return a+b

def mul(a,b):
    return a*b

if __name__ == '__main__':
    print(add(10,20))
    print(mul(10,20))
