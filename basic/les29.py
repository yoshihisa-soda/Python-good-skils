# 名前空間とスコープ

animal = 'cat'

def f():
    # print(animal)
    animal = 'dog'
    print('local:', locals())
f()
print('global:', globals())