#44

'''
import math
print(math.pi)

print(math.sqrt(4.0))

print(math.sqrt(2.0))
'''

'''
import math as m
print(m.pi)
print(m.sqrt(4.0))
print(m.sqrt(2.0))
'''

'''
from math import pi
print(pi)

from math import sqrt
print(sqrt(4.0))
'''

'''
from math import pi, sqrt
print(pi)
print(sqrt(4.0))


from math import sqrt as s
print(s(4.0))
'''
'''
from math import pi as p, sqrt as s
print(p)
print(s(4.0))
'''

import urllib.request
response = urllib.request.urlopen('https://www.google.com')
print("1",response.status)

import urllib.request as r
response = r.urlopen('https://www.google.com')
print("2",response.status)

from urllib.request import Request, urlopen
req = Request('https://www.google.com')
response = urlopen(req)
print("3",response.status)

from urllib.request import *
req = Request('https://www.google.com')
response = urlopen(req)
print("4",response.status)

from urllib.request import Request as r, urlopen as u
req = r('https://www.google.com')
response = u(req)
print("5",response.status)

'''
window cmd
pip install 패키지
'''

import requests
r = requests.get('https://www.google.com')
print("6",r.status_code)