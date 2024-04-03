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


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_animals(self):
        for animal in self.animals:
            print(f"Имя: {animal.name}, Возраст: {animal.age}")

    def show_employees(self):
        for employee in self.employees:
            print(f"Имя: {employee.name}, Профессия: {employee.position}")


class ZooKeeper:
    def __init__(self, name):
        self.name = name
        self.position = "ZooKeeper"

    def feed_animal(self, animal_name):
        print(f"{self.name} кормит {animal_name}")


class Veterinarian:
    def __init__(self, name):
        self.name = name
        self.position = "Veterinarian"

    def heal_animal(self, animal_name):
        print(f"{self.name} лечит {animal_name}")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


bird = Bird("Кукушка", 3, 'коричневый')
mammal = Mammal('Волк', 5, 'лес')
reptile = Reptile('Крокодил', 3, 'река')

zoo_keeper = ZooKeeper('Артем')

veterinarian = Veterinarian('Виктор')

zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
zoo.add_employee(zoo_keeper)
zoo.add_employee(veterinarian)

print("Животные в зоопарке:")
zoo.show_animals()

print("\nСотрудники зоопарка:")
zoo.show_employees()

print("\nГолоса животных:")
animal_sound([bird, mammal, reptile])

zoo_keeper.feed_animal("Волк")
veterinarian.heal_animal("Крокодил")
