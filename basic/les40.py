# クラスの継承

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model s',
                 enable_auto_run=False,
                 password='123'):
        # self.models = models
        super().__init__(model)
        self.password = password

        self._enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        self._enable_auto_run = is_enable
        if self.password == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto run')

car = Car()
car.run()
print('#######################')
toyota_car = ToyotaCar()
print(toyota_car.model)
toyota_car.run()
print('#######################')
tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()



# 注意点

class T(object):
    pass

t = T()
t.name = 'Mike'
t.age = 20
print(t.name, t.age)