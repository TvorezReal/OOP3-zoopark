# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и
# вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические
# методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
# 6. Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке
# в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f'{self.name} издает звуки')

    def eat(self):
        print(f'{self.name} кормится')

class Bird(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def make_sound(self):
        print(f'{self.name} чирикает')

class Mammal(Animal):
    def __init__(self, name, age, habitat):
        super().__init__(name, age)
        self.habitat = habitat

class Reptile(Animal):
    def __init__(self, name, age, habitat):
        super().__init__(name, age)
        self.habitat = habitat

    def make_sound(self):
        print(f'{self.name} ревет')


class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        animal.eat()


class Veterinarian:
    def __init__(self, name):
        self.name = name


    def heal_animal(self, animal):
        animal.make_sound()

class Zoo:
    def __init__(self):
        self.animals = Animal
        self.zoo_keeper = ZooKeeper
        self.veterinarian = Veterinarian

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_zoo_keeper(self, zoo_keeper):
        self.zoo_keeper.append(zoo_keeper)

    def add_veterinarian(self, veterinarian):
        self.veterinarian.append(veterinarian)


 animals = [Bird('Кукушка', 2, 'коричневый'), Mammal('Волк', 5, 'лес'), Reptile('Крокодил', 3, 'река')]

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()