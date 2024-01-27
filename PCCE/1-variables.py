# Variables
# 변수의 할당
# 변수에 어떤 값을 저장하는 것
# 단, 값을 직접 저장하지는 않고, "참조"를 저장한다. 

x = 10
y = x

print(f'x = {x}') # f stands for formatting 
print(f'y = {y}')

# 변수의 삭제 - 삭제된 후에는 해당 변수를 사용할 수 없다. 
del x
# print(f'x = {x}')
print(f'y = {y}') # y는 잘 출력됨. 

x = None # None은 아무것도 들어있지 않다를 의미(변수가 없는 것이 아니라 존재하지만 내용이 없다)
y = 3 # y 변수에 새로운 값을 재할당 

print(f'x = {x}') 
print(f'y = {y}')

# special for Python: 다중 변수 할당
x, y, z = 10, 20, 30 # 개수 상관 없이 ,로만 구분
print(f'x = {x}')
print(f'y = {y}')
print(f'z = {z}')

# 좌변과 우변의 개수가 다른 경우: error
# 좌변이 하나인 경우에만 정상 동작 (여러 값을 동시에 저장, 튜플)
# x, y = 1, 2, 3
# print(f'x = {x}')
# cf. 
x = 1, 2, 3
print(f'x = {x}')

# 변수를 교차로 쓰면 서로 교체 가능 (= Swap / 다중 할당이 가능하기 때문)
x, y = 10, 20
x, y = y, x
print(f'x = {x}')
print(f'y = {y}')

# cf. 다중 할당이 불가능한 경우 Swap 구현(C, C++, Java, JavaScript...)
x = 10
y = 30

temp = x
x = y
y = temp
print(f'x = {x}')
print(f'y = {y}')
















