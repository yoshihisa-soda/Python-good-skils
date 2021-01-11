# 引数の使い方

def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)



menu(entree='beef', drink='beer', dessert='ice')
print(r)

# [1, 2, 3, 100]と出力
# 参照渡しをデフォルトで置いておくとバグにつながる
# def test_func(x, l=[]):
def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

# y = [1, 2, 3]
# r = test_func(100, y)

r = test_func(100)
print(r)
r = test_func(100)
print(r)