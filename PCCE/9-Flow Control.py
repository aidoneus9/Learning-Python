# 조건문

# if 문
# 조건이 참이면 실행문을 실행하는 조건문
# 조건이 거짓이면 실행문을 건너뛴다. 
x = 10
if x > 5:
    print('x는 5보다 크다.') # 이 코드들이 실행된다(들여쓰기된 코드들)
    print('그래서, 조건문이 참이다.')
print('무조건 실행되는 코드') # 조건의 참/거짓 상관없이 항상 실행된다. 

x = 1000
if not 0 <= x <= 100:
    x = float('nan')
print('정수는 {}점 입니다.'.format(x))


# if ~ else 문
# 양자택일로 동작하는 조건문
x = 120
if x > 100:
    x = 100
else:
    x = x
print('정수는 {}점 입니다.'.format(x))

# if ~ elif ~ else 문
# 여러 조건을 연쇄적으로 참/거짓을 판별하는 조건문
# else가 없으면 아무 실행문도 실행되지 않을 수 있다. 
x = 50
if x > 100:
    x = 100
elif x < 0:
    x = 0
else:
    x = x
print('정수는 {}점 입니다.'.format(x))

# Nested if(중첩된 if 문)
math = 100
eng = 100
if math >= 60:
    if eng >= 60:
        print('1.합격입니다.')
    else:
        print('2.영어 점수 미달입니다.')
else:
    if eng >= 60:
        print('3.수학 점수 미달입니다.')
    else:
        print('4.두 과목 모두 미달입니다.')

# 조건 표현식(ternary operator에 해당)
# if ~ else 문을 한 줄로 줄이는 방법 
# 항상 되는 것은 아니고, 변수에 표현식을 대입하는 경우에만 가능
x = 120
x = 100 if x > 100 else x
print(f'x = {x}')

# for 반복문(for Loop)
# range는 슬라이상과 유사하게, 시작점, 끝점+1, step을 입력받는다. 
for i in range(10): # i라는 변수를 0부터 9까지 총 10번 반복 
    print(i, end=' ') # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 / end='\n'
print()

for i in range(2, 8): # i라는 변수를 2부터 8전까지 총 8-2번 반복(2~7)
    print(i, end=' ') # 2, 3, 4, 5, 6, 7
print()

for i in range(2, 10, 3): #i라는 변수를 2부터 10전까지 3씩 증가하면서 반복
    print(i, end=' ') # 2, 5, 8
print()

# for문 반복자 -> 리스트, 튜플, 문자열, 집합, 딕셔너리
x = [10, 20, 30, 40]
for i in x: # range 대신 반복자를 쓸 수 있다.
    print(i, end=' ') 
print()

x = {'a': 100, 'b': 200, 'c': 300}
for key in x: # 딕셔너리는 반복하면 key를 하나씩 순회한다. 순회: 전체 자료를 한 번씩 다 훑는다. 
    print(key, x[key]) # key를 이용해서 쌍인 value도 가져올 수 있다.

# 중첩된 for 문
# if 문이 중첩되듯, for 문도 중첩 가능 
for i in range(3): # i -> 0, 1, 2
    for j in range(2): # j -> 0, 1
        print((i, j)) # 3*2 = 6번 반복 
print()

# zip을 이용한 for 문
a = [1, 2, 3]
b = [4, 5, 6]

# 2중 for 문 - 모든 조합을 전부 다 반복 
for i in a: 
    for j in b:
        print((i, j))
print()

# zip을 이용한 for 문 - 같은 인덱스끼리만 반복
for i, j in zip(a, b):
    print(i, j)
print()

# enumerate을 이용한 for 문(zip과 비슷) - 값과 인덱스를 동시에 반복
x = [10, 20, 30, 40, 50]
for i, val in enumerate(x):
    print(i, val)

# 대부분의 언어는 아래와 같은 방법으로 접근 
for i in range(len(x)):
    val = x[i]
    print(i, val)

# while 문을 이용한 반복
# 반복 횟수가 정해져 있지 않다.
# cf) for 문은 반복횟수가 정해져 있다.
# 무한루프가 되면 Ctrl + C로 정지 가능
# for -> while 변환은 가능하나, while -> for 변환은 불가능할 수도 있다. 
x = 10
while x < 100:
    print(x)
    x += 10

# while True:
#     print('무한루프') 

# for 문 -> while 문 변환    
for i in range(2, 10):
    print(i)

i = 2
while i < 10:
    print(i)
    i += 1

# 반복문의 제어문 
# break, continue

# break는 즉시 반복문을 종료, for 문이나 while 문 모두 가능
for i in range(10):
    if i == 3:
        break
    print(i) # 0, 1, 2 
print()

# continue는 현재 실행문만 건너뛰고 다음 반복으로 넘어감 
for i in range(10):
    if i == 3:
        continue
    print(i) # 0, 1, 2, 4, 5, 6, 7, 8, 9 (3만 빼고)

for i in range(3):
    for j in range(3):
        if j == 1:
            break # 가장 가까운 반복문에 동작함 (j-for문)
        print(i,j) # 0 0, 1 0, 2 0

for i in range(3):
    for j in range(3):
        if j == 1:
            continue # 가장 가까운 반복문에 동작함 (j-for문)
        print(i,j) 

# 가장 가까운 for문과 더불어, 바깥쪽 for문도 종료하고 싶을 때 
for i in range(3):
    is_done = False

    for j in range(3):
        if j == 1:
            is_done = True #
            break
        print(i, j)

    if is_done is True: #
        break
print()

# 지능형 리스트
# List Comprehension
# for 문과 유사한 문법으로 리스트를 손쉽게 생성

# 0 2 4 6 8 ... 18 를 요소로 가지는 리스트를 만들어보자.
x = []
for i in range(10): #for in range(0, 20, 2)
    x.append(2*i)
print(x)

x = [2*i for i in range(10)]
print(x)

# Truthy, Falsy 값
# if, while에 truthy, falsy(비어있거나, none, 0)
x = [1, 2, 3, 4, 5] # truthy
while x:
    val = x.pop() # 값이 하나씩 빠져나가다가 텅 비게 되면, while 문의 x가 falsy 값이 되면서 종료함
    print(val)

x = None # None은 Falsy 값
if not x: # (not) Falsy 값이면 강제로 0으로 값을 변경
    x = 0
print(x)

