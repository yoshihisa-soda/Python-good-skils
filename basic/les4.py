r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3))

print(r.count(3))

if 5 in r:
    print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)

s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)

x = ' '.join(to_split)
print(x)

i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print()

z = [1, 2, 3, 4, 5]
y = z.copy()
y[0] = 100
print(z)
print(y)