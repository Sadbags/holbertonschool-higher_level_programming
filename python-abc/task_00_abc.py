from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class dog(Animal):
    def sound(self):
        return 'bark'


class cat(Animal):
    def sound(self):
        return 'meow'
