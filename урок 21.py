# class Car:
#
#     def __str__(self):
#         return "Car class Object"
#     # создание методов класса
#     def start(self):
#         print("Двигатель заведен")
#
# car_a = Car()
# car_b = Car()
# print(car_a)
# print(car_b)


# class Phone:  # класс Телефон
#     def __init__(self, color, model): # инициализатор конструктора
#         self.color = color   # динамические свойства цвет и модель
#         self.model = model
          #Метод класса
         # Принимает 1) ссылку на класс Phone и 2) цвет в качестве параметров
         # Создает специфический объект класса Phone(особенность объекта в том, что это игрушечный телефон)
         # При этом вызывается инициализатор класса Phone
         # которому в качестве аргументов мы передаем цвет и модель,
         # соответствующую созданию игрушечного телефона

#         # обычный метод
#         # первый параметр метода - self
#
#     def check_sim(self, mobile_operator):
#         if self.model == '1785' and mobile_operator == 'MTS':
#             print('Your mobile operator is MTS')
#
       # Статический метод справочного характера
       # Возвращает хэш по номеру модели
       # self внутри метода отсутствует

#     @staticmethod
#     def model_hash(m):
#         print('Статический метод', m)
#
#     @classmethod
#     def toy_phone(cls, c):
#         toy_phone = cls(c, 'ToyPhone')
#         return toy_phone  # возврат переменной
#
# my_phone = Phone('red', '1785') # объект класса телефон
# my_phone.check_sim('MTS')
# my_phone.model_hash('модель')
# Phone.model_hash('модель')
# print(Phone.toy_phone('Red').model)

# Создайте класс Human.
# Определите для него два статических поля: default_name и default_age.
# Создайте метод __init__(), который помимо self принимает еще два параметра: name и age.
# Для этих параметров задайте значения по умолчанию, используя свойства default_name и default_age.
# В методе __init__() определите четыре свойства: Публичные - name и age. Приватные - money и house.
# Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.
# Реализуйте справочный статический метод default_info(),
# который будет выводить статические поля default_name и default_age.
# Реализуйте метод earn_money(), увеличивающий значение свойства money.
class Human:
    # Статические поля
    default_name = 'John'
    default_age = 30

    def __init__(self, name=default_name, age=default_age):
        # Динамические поля
        # Публичные
        self.name = name
        self.age = age
        # Приватные
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Name:{self.name}, age:{self.age}\n'
              f'House:{self.__house}, money:{self.__money}')

    # Статический метод
    @staticmethod
    def default_info():
        print(f'Default Name: {Human.default_name}')
        print(f'Default Age: {Human.default_age}')

    def earn_money(self, amount):
        self.__money += amount
        print(f'Earned {amount} money! Current value: {self.__money}')

Human.default_info()

alexander = Human('Sasha', 27)
alexander.info()

alexander.earn_money(5000)
alexander.earn_money(20000)
alexander.info()

    # print(alexander._Human__house)

# class Phone:
#
#     def __init__(self):
#         self.is_on = False
#
#     def turn_on(self):
#         self.is_on = True
#
#     def call(self):
#         if self.is_on:
#             print('Making call...')
#
#     def info(self):
#         print(f'Class name: {Phone.__name__}')
#         print(f'If phone is ON: {self.is_on}')
#
# class MobilePhone(Phone):
#
#     def __init__(self):
#         super().__init__()
#         self.battery = 0
#
#     # def charge(self, num):
#
#     def info(self):
#         print(f'Class name: {Phone.__name__}')
#         print(f'If phone is ON: {self.is_on}')
#         print(f'Battery level: {self.battery}')
#
#     def show_polymorphism():
#         for a in [Phone, MobilePhone]:
#             print('------------')
#             object = a()
#             object.info()
#
#     show_polymorphism()


# class Vehicle:
#     def vehicle_method(self):
#         print('Это родительский метод из класса Vehicle')
#
# class Car(Vehicle):
#      def car_method(self):
#          print('Это дочерний метод из класса Car' )
#
# class Cycle(Vehicle):
#     def cycleMethod(self):
#         print('      ')


# class Camera:
#     def camera_method(self):
#         print("Camera")
#
# class Radio:
#     def radio_method(self):
#         print('Radio')
#
# class CellPhone(Camera, Radio):
#     def cell_phone_method(self):
#         print('CellPhone')
#
# cell_phone_a = CellPhone
# cell_phone_a.camera_method()
# cell_phone_a.radio_method()

# class House:
#     def __init__(self, area, price):
#         self.area = area
#         self.price = price
#
#     def final_price(self, discount):
#         final_price = self._price * (100 - discount)/100
