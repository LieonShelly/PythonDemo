# python是动态语言
print("hello world")
name = "lieon"
print(name)
name1 = name
name = "pao"
print(name1)
if name == name1:
    print("equal")
elif name != name1:
    print("....")
else:
    print("not equal")

count = 0
my_integers = [5,2,123,1231,123]
print(my_integers[0])
releatives_names = [
    "Toshaasf",
     "asdf",
     "Yuji",
     "Bruno",
     "Kaio"
]
bookself = []
bookself.append("asf")
bookself.append("sfa")
# Dictionary
dictionary_example = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
dictionary_tk = {
    "name": "Leandro",
    "nickiname": "TK",
    "nationality": "Brazilian"
}
print("my name is %s" %(dictionary_tk["name"]))
dictionary_tk["age"] = 24
for book in bookself:
    print(book)

for key in dictionary_tk:
    print("%s --> %s" % (key, dictionary_tk[key]))

for key, value in dictionary_tk.items():
    print("%s -----> %s" % (key, value))

################ CLASS ###########################
class Vehicle:
    pass
class Vehicle:
    def __init__(self, number_of_wheels, type_of_trunk, seating_capacity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_trunk
        self.seating_capacity = seating_capacity

    def number_of_wheels(self):
          return  4

    def set_number_of_wheels(self, number):
        self.number_of_wheels = number

        @property
        def number_of_wheels(self):
            return  self.number_of_wheels

        @number_of_wheels.setter
        def number_of_wheels(self, number):
            self.number_of_wheels = number

    def make_noise(self):
        print('VARRRRRR')
tesla_model_s =  Vehicle(4,"electric",5)
print(tesla_model_s.number_of_wheels)
tesla_model_s.make_noise()

class Person:
    first_name = 'TK'
    # non-public
    _email = 'private email'

    def show_age(self):
        return  self._email
    #non-public method
    def _show_emali(self):
        return self._email

class Car:
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

class ElectriCar(Car):
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        Car.__init__(self, number_of_wheels, seating_capacity, maximum_velocity)

class Dog:

    def __init__(self): #构造方法
    def __del__(self): #析构方法
    def __call__(self, *args, **kwargs):# 对象后加括号时调用
    @staticmethod
    def eat(self):
        print("asdf")

    @classmethod
    def bark(self):
        print ("asdfas")
    @property
    def flight_status(self):
        print ('drik')
    @flight_status.setter
    def flight_status(self,status):
        print ('drik')
    @flight_status.deleter
    def flight_status(self):
        print ('drik')

d = Dog()
d.eat(d)
d.flight_status = 2;
print(Dog.__doc__) #输出类的描述信息
print(d.__module__) # 输出改动对象所在的模块
print(d.__class__) # 输出该对象的类

class Foo:
    def __getitem__(self, key):
        print('__getitem__', key)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)

    def __delitem__(self, key):
        print('__delitem__',key)

    def __init__(self,name):
        self.name = name

obj = Foo()
result = obj['k1'] #  # 自动触发执行 __getitem__
obj['k2'] = 'lieon'  # 自动触发执行 __setitem__
del  obj['k1']

class MyType(type):
    def __init__(self, *args, **kwargs):
        print("Mytype __init___", *args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("Mytype __call__", *args, ** kwargs)
        obj = self.__new__(self)


