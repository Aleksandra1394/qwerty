a=lambda a, b, c , d : a + b + c +d
print(a(3, 5, 4, 8))


s=lambda w , e : w / e
print(s(16, 2))

a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[0])
print(a)

a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print(a)

