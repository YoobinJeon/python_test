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