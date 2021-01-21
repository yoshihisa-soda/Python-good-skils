import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    # これがある場所は、全て定義しなければいけない
    # あまり使用しなくても良い
    # コードスタイル的には必要ないことが多い
    @abc.abstractmethod
    def drive(self):
        pass

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        if sekf.age >= 18:
            print('ok')
        else:
            raise Exception('No drive')

class Adalt(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        print('drive')

baby = Baby()
adult = Adalt()


class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    def ride(self, person):
        person.drive()

car = Car()
car.ride(adult)