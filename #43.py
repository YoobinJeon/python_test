#43.3
import re

'''
m = re.match('([0-9]+) ([0-9]+)', '10 295')

print(m.group(1))

print(m.group(2))

print(m.group())
'''

'''
m = re.match('(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<arg>\w+)\)', 'print(1234)')

print(m.group('func'))
print(m.group('arg'))

print(re.findall('[0-9]+', '1 2 Fizz 4 Buzz Fizz 7 8'))
'''

#re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)
print(re.sub('apple|orange', 'fruit', 'apple box orange tree'))

print(re.sub('[0-9]+', 'n', '1 2 Fizz 4 Buzz Fizz 7 8'))


def multiple10(m):
    n = int(m.group())
    return str(n*10)

print(re.sub('[0-9]+', multiple10, '1 2 Fizz 4 Buzz Fizz 7 8'))