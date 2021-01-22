class Person(object):

    kind = 'human'

    def __init__(self):
        self.x = 100

    # classメソッド self -> cls
    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    # staticメソッド
    @staticmethod
    def about(self):
        print('about human {}'.format(year))

a = Person()
print(a.what_is_your_kind())

# これはオブジェクトになっていない状態
# b = Person
# print(b)

print('###################3')
print(Person.kind)
print(Person.what_is_your_kind())

Person.about(1999)