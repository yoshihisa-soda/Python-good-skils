chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('B')

print(chose_from_two)
print(answer)

dict(a=10, b=20)

d = {'x': 100, 'y': 200}
dk = d.keys()
dv = d.values()
print(dk, dv)

d.pop('x')
print(d)
del d['y']
print(d)

# リストはkeyのvalueを検索するのにプログラムが冗長になる
# 辞書型を使うべき

fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300
}

print(fruits['apple'])
