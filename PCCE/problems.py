# # 1
# x = [-1, 3, 5, 6, 2, 18, -34, 5]
# answer = (sum(x) / len(x))
# print(answer)

# # 2 
# x = [0, 1, 2, 3, 4, 5]
# answer = x + x[::-1] # reverse를 하면 리스트를 수정하게 됨. 슬라이싱을 하면 새로운 리스트를 만든다. 
# print(answer)

# # 3
# x = [-4, 2, -5, -5, 3, 7, 3, -2, 5, -5, 8]
# answer = len(set(x))
# print(answer)

# # 4
# x = (5, 2, 0, 6, 3, 1, 9, 10)

# # 방법1 - C언어 같은 스타일
# y = list(x)
# y.sort(reverse=True)
# answer = tuple(y)
# print(answer)
 
# # 방법2 - Pythonic한 스타일 
# answer = tuple(sorted(x, reverse=True)) # sorted: 어떤 것이든 받아서 정렬 후 리스트로 만들어 줌
# print(answer) 

# 5 
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = x[:2]
y.reverse()
# print(y[::-1])
# print(y.reverse()) # None가 아니라 reverse를 하고 print(y) 
z = x[2:4]
h = x[4:6]
l = x[6:8]
g = x[8:10]
z.reverse(), h.reverse(), l.reverse(), g.reverse()
# k = y[::-1] + z[::-1] + h[::-1] + l[::-1] + g[::-1]
k = y + z + h + l + g
print(k)

# 슬라이싱?
# 변수 스왑 이용 
# 1. 다 잘라서 조각으로 만듦 -> 2. 위치를 바꿈 

# # 6.
# x = 'abcdef'
# y = 'ghijkl'
# z = [0] * (len(x) + len(y)) # 0 또는 None
# z[::2] = x # 0, 2, 4, .... <- x 
# z[1::2] = y # 1, 3, 5, ... <- y
# answer = ''.join(z)
# print(answer)

#7
# 0015 # 14.52
x = 15
y = 14.52142


