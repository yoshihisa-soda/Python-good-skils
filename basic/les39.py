#クラスの定義

# objectなどの引数を入れなくても良いが、書いておいたほうがいい。

class Person(object):
    def say_something(self):
       print('hello')

person = Person()
person.say_something()


# クラスの初期化とクラス変数
# メソッドの引数にはselfを必ず入れる

class Person(object):
    def __init__(self, name):
        self.name = name
        print('First')

    def say_something(self):
        print('I am {} .hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run' * num)

    def __del__(self):
        print('good bye')

person = Person('Mike')
person.say_something()

del person

# 「#############」の前にgood byeが呼ばれる
print('################')

