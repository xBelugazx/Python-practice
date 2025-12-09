'''
형변환

2 + '2' = 불가능
why? 숫자 + 문자이기 때문
이럴 때 형변환을 씀
'''

# 괄호 안에 바꾸려는 값 or 변수넣기
# 단, 괄호 안의 값은 변환하려는 자료형이 알 수 있는 값이어야 함
int('2') # 정수로
# int('two') 불가능

float('3.14') # 실수로
str(2) # 문자로

'''
int('3.14')
'''
int(float('3.14')) # 3
# 실수 -> 정수, 소수점 이하 부분은 반올림이 아닌 버림이 됨.

# 산술 연산자
# 더하기 빼기 곱하기 나누기
print(1 + 2)
print(10 - 2)
print(2 * 5)
print(10 / 3) # 부동소수점 형태로 반환

# 나머지 몫 거듭제곱
print(5 % 2)
print(5 // 2) # 정수 반환
print(5 ** 2)

# 비교 연산자
print(5 > 2)
print(5 >= 10)
print(4 < 10)
print(4 <= 4)
print(5 == 1)
print(2 != 10)

# 논리 연산자
print(3 != 2 and 5 == 5)
print(2 != 2 or 7 > 2)
print(not 3 > 2) # 반전 

# 멤버 연산자
# 어떤 값이 그룹에 포함돼있니?
print('e' in 'heihachi')
print('z' not in 'samsung')

'''
불리안 연산자

bool()
불리안으로 형변환

값 O = True
값 X = False
'''
a = 'Hello' # 값 O
b = '     ' # 빈칸이란 값이 O
c = "" # 값 X

print(bool(a))
print(bool(b))
print(bool(c))

a = 1 # 값 O
b = -19 # 값 O
c = 0 # 값 X

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(None))
# None: 값이 없다는 키워드
