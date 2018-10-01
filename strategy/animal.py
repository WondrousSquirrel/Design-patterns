from strategy import CatNoiseStrategy
from strategy import DogNoiseStrategy
from strategy import HighFlyStrategy

catNoise = CatNoiseStrategy()
dogNoise = DogNoiseStrategy()
highFly = HighFlyStrategy()

class Animal(object):
    def __init__(self, noise_strategy, fly_strategy):
        self.noise_strategy = noise_strategy
        self.fly_strategy = fly_strategy
    
    def noise(self):
        self.noise_strategy.noise()
    
    def fly(self):
        self.fly_strategy.fly()

# Типы животных
'''
Кот, как и собака - не может летать самостоятельно, по этому
функция fly - будет отсутствовать
'''
class Cat(Animal):
    def __init__(self):
        super(Cat, self).__init__(catNoise, None)
    
    def jump(self):
        print('Very High Jump')

class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__(dogNoise, None)
    
    def jump(self):
        print('Jump on a sofa')

class Bird(Animal):
    def __init__(self):
        super(Bird, self).__init__(None, highFly)


cat = Cat()
dog = Dog()

cat.noise()
dog.noise()
