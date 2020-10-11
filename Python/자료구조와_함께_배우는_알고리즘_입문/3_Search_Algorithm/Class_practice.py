class Person:

    def __init__(self, name, age, address):
        self.hello = '안녕하세요'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print(f'{self.hello}. 저는 {self.name}입니다.')

maria = Person('마리아', 20, '전주시 강남구 성포동')
maria.greeting()

print('이름: ', maria.name)
print('나이: ', maria.age)
print('주소: ', maria.address, '\n')

class Square:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

square1 = Square(10, 5, 'red')
print(square1.width, square1.height, square1.color)

square2 = Square(7, 7, 'blue')
print(square2.width, square2.height, square2.color, '\n')

class AnotherSquare:
    width = 0
    height = 0
    color = 0

    def get_area(self):
        return self.width * self.height

    def set_area(self, data1, data2):
        self.height = data1
        self.width = data2

square3 = AnotherSquare()
square3.set_area(5, 5)
print(square3.width)
print(square3.get_area())