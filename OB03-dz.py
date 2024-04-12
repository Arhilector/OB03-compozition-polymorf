# #1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы
# (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и
# вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
#


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print("Чикчирик")

class Mammal(Animal):
    def make_sound(self):
        print("РРРРР")

class Reptile(Animal):
    def make_sound(self):
        print("Шшшшшшшшш")

reptile = Reptile("Рептилия Петя", 5)
mammal = Mammal("Мартышка Вася", 2)
bird = Bird("Воробушек Маша", 1)

animals = [reptile, bird, mammal]  # передаем созданные объекты в список
for animal in animals:
    animal.make_sound()

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")

class Veterinarian:
    def __init__(self, name):
            self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")

keeper = ZooKeeper("Иннокентий")
vet = Veterinarian("Ветеринар Лариса")

# Создаем зоопарк и добавляем в него животных и сотрудников
zoo = Zoo()
zoo.add_animal(reptile)
zoo.add_animal(bird)
zoo.add_animal(mammal)

zoo.add_employee(keeper)
zoo.add_employee(vet)

# Пример действий сотрудников
keeper.feed_animal(bird)
vet.heal_animal(mammal)




