# Number
# includes integer, float, complex
# integer: 다른 언어와 달리 값의 범위가 무한하다. 

print("integer")
x = 10
print(f'x = {x}')
y = -2000
print(f'y = {y}')

# 정수형 값은 범위가 무제한
import sys
sys.set_int_max_str_digits(999999999)
x = 9999**9999 # 9999의 9999 거듭제곱 
print(f'x = {x}') 
# 대부분 다른 언어의 범위는 2**31 - 1 또는 2**63 - 1

# 정확한 0 값이 존재한다. 
x = 0
print(f'x = {x}')

print('float')
# float 0는 정확한 0일까?
x = 0.000000000 # 실수출력시 유효숫자까지 고려되지는 않음 
print(f'x = {x}')

print(0 == 0.0) # True: 즉, 0.0은 정수 0과 완전히 같은 값으로 친다(python만)

# 실수의 자릿수 표현 방법
x = 1.45
y = 1_452.52 # 실수, 정수 모두 _(underscore)로 자릿수(보통 세 자리수씩)를 끊어 표현 가능/,를 쓰면 튜플이 됨
y = 1_452
z = 142e03 # 142000.0: 142*(10**3) (science notation, 과학표기법)
print(f'z = {z}')
z = -142E-03 # 142000.0: -142*10**-3 (science notation, 과학표기법)
print(f'z = {z}')

# 특수한 실수값 
x = float('nan') # stands for not a number/nan이라는 숫자임 e.g) 0으로 나누는 등 불가능한 계산, 계산이 잘못되었을 때
y = float('inf') # stands for infinity # 종종 사용함(min을 찾을 때 초기화 시) # infinity(not defined) 
z = float('-inf')
print(f'x = {x}')
print(f'y = {y}')
print(f'z = {z}')

# complex
x = 3 + 2j # 실수부가 3이고, 허수부가 2인 복소수
# y = 4 + 8i # i로는 허수부 표현이 안된다. 
print(f'x = {x}')