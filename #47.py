'''
print(bin(13))

print(int('1101',2))

print(bin(0b1101 & 0b1001))

print(0b0011 << 2)

print(bin(12))

print(bytes(10))

print(bytes([10,20,30,40,50]))

print(bytes(b'hello'))

print('hello'.encode())

print('안녕'.encode('euc-kr'))

print('안녕'.encode('utf-8'))
'''
#euc-kr은 한글 표준 인코딩임. 

import time
print(time.time())

print(time.localtime(time.time()))

print(time.strftime('%Y-%m-%d', time.localtime(time.time())))

print(time.strftime('%c', time.localtime(time.time())))

#false
print(0.1 + 0.2 == 0.3)

#47.7
import math, sys
x = 0.1 + 0.2
print(math.fabs(x-0.3) <= sys.float_info.epsilon)

from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))

from fractions import Fraction
print(Fraction('10/3'))

#47.8
class OpenHello:
    def __enter__(self):
        self.file = open('hello.txt', 'w')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with OpenHello() as f:
    f.write('hello')

#47.9
class Singleton(type):       # type을 상속받음
    __instances = {}         # 클래스의 인스턴스를 저장할 속성
    def __call__(cls, *args, **kwargs):    # 클래스로 인스턴스를 만들 때 호출되는 메서드
        if cls not in cls.__instances:     # 클래스로 인스턴스를 생성하지 않았는지 확인
            cls.__instances[cls] = super().__call__(*args, **kwargs)
                                           # 생성하지 않았으면 인스턴스를 생성하여 속성에 저장
        return cls.__instances[cls]        # 클래스로 인스턴스를 생성했으면 인스턴스 반환

class Hello(metaclass=Singleton):    # 메타클래스로 Singleton을 지정
    pass

a = Hello()    # 클래스 Hello로 인스턴스 a 생성
b = Hello()    # 클래스 Hello로 인스턴스 b 생성
print('47.9 :',a is b)  # True: 인스턴스 a와 b는 같음

#47.10
'''
import asyncio

async def hello():    # async def로 네이티브 코루틴을 만듦
    print('Hello, world!')

loop = asyncio.get_event_loop()          # 이벤트 루프를 얻음
loop.run_until_complete(hello())         # hello가 끝날 때까지 기다림
loop.close()                             # 이벤트 루프를 닫음
'''

'''
import asyncio

async def add(a, b):
    print('add: {0} + {1}'.format(a, b))
    await asyncio.sleep(1.0)    # 1초 대기. asyncio.sleep도 네이티브 코루틴
    return a + b                # 두 수를 더한 결과 반환

async def print_add(a, b):
    result = await add(a, b)    # await로 다른 네이티브 코루틴 실행하고 반환값을 변수에 저장
    print('print_add: {0} + {1} = {2}'.format(a, b, result))

loop = asyncio.get_event_loop()          # 이벤트 루프를 얻음
loop.run_until_complete(print_add(1, 2)) # print_add가 끝날 때까지 이벤트 루프를 실행
loop.close()                             # 이벤트 루프를 닫음
'''

# urlopen.py
'''
from time import time
from urllib.request import Request, urlopen

urls = ['https://www.google.co.kr/search?q=' + i
        for i in ['apple', 'pear', 'grape', 'pineapple', 'orange', 'strawberry']]

begin = time()
result = []
for url in urls:
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})  # UA가 없으면 403 에러 발생
    response = urlopen(request)
    page = response.read()
    result.append(len(page))

print(result)
end = time()
print('실행 시간: {0:.3f}초'.format(end - begin))
'''

# asyncio_urlopen.py
from time import time
from urllib.request import Request, urlopen
import asyncio

urls = ['https://www.google.co.kr/search?q=' + i
        for i in ['apple', 'pear', 'grape', 'pineapple', 'orange', 'strawberry']]

async def fetch(url):
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})  # UA가 없으면 403 에러 발생
    response = await loop.run_in_executor(None, urlopen, request)    # run_in_executor 사용
    page = await loop.run_in_executor(None, response.read)           # run_in_executor 사용
    return len(page)

async def main():
    futures = [asyncio.ensure_future(fetch(url)) for url in urls]
                                            # 태스크(퓨처) 객체를 리스트로 만듦
    result = await asyncio.gather(*futures) # 결과를 한꺼번에 가져옴
    print(result)

begin = time()
loop = asyncio.get_event_loop()          # 이벤트 루프를 얻음
loop.run_until_complete(main())          # main이 끝날 때까지 기다림
loop.close()                             # 이벤트 루프를 닫음
end = time()
print('실행 시간: {0:.3f}초'.format(end - begin))

print('hello')
print('hello')
