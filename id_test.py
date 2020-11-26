g = range(10)
print(id(g))
g = range(20)
print(id(g))
print(f'=' * 20)

h = [2, 3, 4]
print(id(h))
h[1] = 10
print(id(h))
print(f'=' * 20)

i = "random"
print(id(i))
i = i + " work"
print(id(i))