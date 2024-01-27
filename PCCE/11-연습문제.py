x = 10
y = 'abc'
z = y + str(x)
print(z)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x[::2], x[1::2] = x[1::2], x[::2]
print(x)

x = 'abcdef'
z = [0] * len(x) * 2
print(z)

x = 15
y = 14.52142
print("%04d%7.2f" % (x, y))