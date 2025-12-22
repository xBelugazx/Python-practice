snack = '맛동산'
drink = '콜라'

print(snack + ' ' + drink)
print(snack, drink) # print(값 or 변수, 값 or 변수)
'''
,는 자동 띄어쓰기로 출력해줌.
'''

# 다른 문장 속에 변수 포함시키기
'''
개발 언어에는 파이썬, 자바 등이 있어요.
'''
# 1. {} + format
python = '파이썬'
java = '자바'

print('개발 언어에는 {}, {} 등이 있어요.'.format(python, java))
print('내가 좋아하는 간식은 {}과 {}야'.format('맛동산', '바나나'))

# 2. {N} + format // N = 0, 1, 2 ...
p9 = '이채영'
p9_ = '송하영'

print('정말 이쁜 아이돌 {0}과 {1}을 모셨습니다.'.format(p9, p9_))
print('정말 이쁜 아이돌 {1}과 {0}을 모셨습니다.'.format(p9, p9_))

# f-string
in_and_out = '인앤아웃'
five = '파이브가이즈'

print(f'미국 최고의 햄버거 집, {in_and_out}과 {five}는 맛있어.')

