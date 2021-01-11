# 位置引数のタプル化
# *args 複数の引数を
def say_something(word, *args):
    print(word)
    for arg in args:
        print(arg)

say_something('Hi', 'Mike', 'Nancy')

# t = ('Mike', 'Nancy')
# say_something('Hi!', t*)


# キーワード引数の辞書化
# **kwargs 辞書型の引数
def menu(**kwargs):
   # print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

# menu(entree='beef', drink='coffee')
d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}
menu(**d)


def sports(s, *args, **kwargs):
    print(s)
    print(args)
    print(kwargs)

sports('tennis', 'swimming', 'baseball', like='basketball', dislike='soccer')


