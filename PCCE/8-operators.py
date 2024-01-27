# x(변수) + 3(리터럴)
# 산술 연산자
# 사칙연산을 포함한 수학적으로 사용되는 연산자

print(14 + 3) # 덧셈은 숫자를 더한다
print([1, 2] + [3, 4]) # 덧셈은 리스트/튜플/문자열을 이어붙인다.
print(7 - 16.0) # 뺄셈은 숫자를 뺀다. 정수와 실수를 계산하면 실수가 된다.
print(5 * 20.0) # 곱셈은 숫자를 곱한다. 
print('abc'*12) # 곱셈은 리스트/튜플/문자열을 반복한다.
print(18 / 6) # 3.0 나눗셈은 기본적으로 실수를 출력한다.
print(18 // 6) # 정수 나눗셈은 //로 표기한다.
print(18 // 10) # 정수 나눗셈은 '몫'을 계산한다. 즉, 소수점 아래는 버린다. 
print(18 % 10) # Modulus 연산은 '나머지'를 계산한다.
print(2 ** 10) # **는 거듭제곱을 의미한다. 
print(-10) # -는 음의 부호를 의미하는 단항 연산자
print(--10) # 10 / -는 연산자이기 때문에 두 개 연달아 붙이면 양수가 된다. 
print(+10) # +는 양의 부호를 의미하는 단항 연산자. 의미없다

# C언어 기반의 언어의 경우
# x = 10
# print(--x) # 9
# print(x) #9

# 비교연산자
# 두 값을 비교해서 True/False를 반환 
x = 10
y = 20
print(x == y) # 두 값이 같으면 True 다르면 False
print(x != y) # 두 값이 다르면 True 같으면 False
print(x < y) # 앞의 값이 더 작으면 True (less than)
print(x <= y) # 앞의 값이 작거나 같으면 True (less than or equal to)
print(x > y) # Greater than
print(x >= y) # Greater than or equal to

# 할당연산자 
# 변수에 값을 할당하는 연산자 
# 좌측에 변수를, 우측에 값을 놓는다. 
x = 20 # x라는 변수에 20이라는 값을 할당하는 할당 연산자 
x += 20 # x = x + 20 을 줄여 쓴 할당 연산자
print(f'x = {x}') # 40
x -= 10 # x = x - 10 을 줄여 쓴 할당 연산자  
print(f'x = {x}') # 30
# 마찬가지로 * / // % ** 전부 가능 

# 논리연산자
# 논리값(True/False)끼리 연산하는 연산자

print(True and True) # True
print(True and False) # False
x = 30
y = 15
print(x > 10 and y > 20)
print(x > 10 or y > 20)
print(not(x > 10 and y >20))
print(0 < x <= 30) # 0 < x and x <= 30을 줄여서 쓴 것(python 가능)

# 멤버연산자
# 좌측의 값이 우측에 속해 있는지 반환하는 연산자
# True/False로 반환한다. 
a = [1, 3, 5, 7, 9] # 리스트/튜플/문자열/집합/딕셔너리 가능 
print(3 in a) # 3이 a에 들어있으면 True
# 딕셔너리의 경우 key만 검사
b = {1: 10, 2: 30, 5: 20}
print(1 in b) # 1이 b의 key에 있으므로 True
print(10 in b) # 1이 b의 key에 없으므로 False
print(10 not in b) # True, not (10 in b)도 되지만, 이렇게도 표현 가능함

# 식별연산자
# 두 피연산자가 동일한 객체(메모리상에 있는 자료)를 가리키는지 검사
# 값뿐 아니라, 실제로 같은 객체여야 함
x = [1, 2, 3, 4]
y = x # y는 x와 같은 객체
z = x[:] # z는 x와 다른 객체 - 슬라이싱 과정에서 새 리스트를 만들어 줌.
print(x is y) # x와 y가 같은 객체이므로 True
print(y is z) # y와 z가 다른 객체이므로 False
print(y is not z) # 다른 객체이면 True

x[2] = 90
print(y)
print(z)

# 연산자의 우선순위: 값 -> 논리 -> 논리끼리 연산 