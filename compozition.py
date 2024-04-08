class Engine():
    def start(self):
        print("двигатель запущен")

    def stop(self):
        print("двигатель остановлен")

class Car():
    def __init__(self):
        self.engine = Engine() # вставили двигател

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()



my_car = Car() # создание объекта

my_car.start()
my_car.stop()