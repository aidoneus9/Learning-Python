numbers = input().split(" ") # 여러 문자열을 문자열 리스트로 변경
numbers = list(map(int, numbers)) # 각 문자열에 int 적용

max_val = float('-inf')
for i in numbers:
    if max_val < i:
        max_val = i
print(max_val)