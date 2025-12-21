s = '욕망이라는 이름의 전차'

print(s.startswith('욕망')) # True
print(s.endswith('징검다리')) # False

s1 = '=====리제로부터 시작하는 이세계====='
s2 = '      리제로부터 시작하는 이세계       '
print(s1.strip('=')) # 문자열 앞 뒤로 불필요한 부분 제거
print(s2.strip()) # 문자열 앞 뒤로 공백 제거

s3 = '스폰지밥과 뚱이'
print(s3.replace('뚱이', "징징이")) # 문자열 일부 변경

s4 = '나도고등학교'
print(s4.find('학교')) # 특정 글자 찾기(인덱스 기준)
print(s4.center(10, '=')) # 문자열을 다른 문자 가운데에 넣기
