# ジェネレーター

l = ['Good Morning', 'Good Afternoon', 'Good Night']

for i in l:
    print(i)

print('############')

def greeting():
    yield 'Good Morning'
    yield 'Good Afternoon'
    yield 'Good Night'

def counter(num=10):
    for _ in range(num):
        yield 'run'
# for g in greeting():
#     print(g)

g = greeting()
c = counter()

print(next(g))
print(next(c))
print('@@@@@@@@@')
print(next(g))
print(next(c))
print('@@@@@@@@@')
print(next(g))
print(next(c))

