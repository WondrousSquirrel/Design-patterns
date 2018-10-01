'''
Паттерн "Стратегия" позволяет использовать функиональность 
в любом классе. Таким образом избегается повторения кода, в параллельных ветках
и сохраняется разное поведение объектов
'''

import abc

class INoiseStrategy(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def noise(self):
        '''Обязательный метод'''


class CatNoiseStrategy(INoiseStrategy):
    def noise(self):
        print('Meow')


class DogNoiseStrategy(INoiseStrategy):
    def noise(self):
        print('Bark!')


class IFlyStrategy(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def fly(self):
        '''Обязательный метод'''


class HighFlyStrategy(IFlyStrategy):
    def fly(self):
        print('Very High')