# 빠르다
# 수학의 집합과 유사한 자료형
# 리스트와 상당히 유사하나, 중복이 허용되지 않는다. 즉, 같은 값은 하나만 존재할 수 있다. 
# 또한 "인덱스" 개념이 존재하지 않는다. 

# 집합의 생성
x = set() # 빈 집합 생성
print(f'x = {x}')

x = {10, 20, 30, 40}
print(f'x = {x}') # 40, 10, 20, 30 입력한 순서대로 출력되지 않음. '순서' 개념이 없음

x = [10, 20, 20, 30, 40, 40, 50, 60, 10]
y = set(x) # 리스트를 집합으로 변환. 중복과 순서가 사라짐(by 내부적 기준)
print(f'y = {y}')

# 집합에 자료 추가하기
x = set()
x.add(4) # 자료 추가하기
x.add(10)
x.add(40)
x.add(4) # 중복된 자료는 추가되지 않는다.
print(f'x = {x}')
# x.update([30, 40, 50]) # 여러 자료를 리스트나 집합 등으로 추가 가능
x.update({30, 40, 50})
print(f'x = {x}')

#잡합에서 자료 제거하기
x = {10, 20, 30, 40, 50, 60}
print(f'x = {x}')
x.remove(30)
print(f'x = {x}')

# 집합의 연산(적용 가능)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f'a.intersection(b) = {a.intersection(b)}') # 교집합
print(f'a & b = {a & b}') # 교집합
print(f'a.union(b) = {a.union(b)}') # 합집합
print(f'a | b = {a | b}') # 합집합
print(f'a.difference(b) = {a.difference(b)}') # a 차집합 b
print(f'a - b = {a - b}') # a 차집합 b
print(f'a ^ b = {a ^ b}') # 대칭차집합 (합집합 - 교집합)

# 빠른 루트: 리스트 -> 집합(중복 제거) -> 리스트 변환