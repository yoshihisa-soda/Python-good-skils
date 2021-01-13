# ジェネレーター内包表記

def g():
    for i in range(10):
        yield i

g = g()
g = tuple(i for i in range(10) if i % 2 == 0)
print(type(g))
print(g)

