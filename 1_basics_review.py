# # a = [1  # item1
# #     , 2]
# # print(a)
# #
# # b = {'key1': 1 #comment1
# # ,'key2': 2 # comment2
# # }
# # print(b)
# # a = 10
# # b = 20
# # c = 30
# # if a > 5 \
# #     and b > 10 \
# #         and c > 20:
# #     print('yes')
# #
# # lambda x: x**2
# # func_1 = lambda x: print(x**2)
# # func_1(2)
#
# # min_lenght = 2
# #
# # while True:
# #     name = input("Please enter your name: ")
# #     if len(name) >= min_lenght and name.isprintable() and name.isalpha():
# #         break
# #
# # print(f'Hello, {name}')
# #
# # a = 0
# #
# # while a < 10:
# #     a += 1
# #     if a % 2 == 0:
# #         continue # ignores
# #     print(a)
# #
# # l = [1,2,3]
# # val = 10
# #
# # found = False
# # index = 0
# #
# # while index < len(l):
# #     if l[index] == val:
# #         found = True
# #         break
# #     index += 1
# #
# # if not found:
# #     l.append(val)
# # print(l)
#
# # a = 10
# # b = 0
# #
# # try:
# #     a / b
# # except ZeroDivisionError:
# #     print('division by 0')
# # finally:
# #     print('this always executes')
#
# # for i in range(1, 10):
# #     print(i)
# #     if i % 7 == 0:
# #         print('multiple of 7 found')
# #         break
# #     else:
# #         print("no multiple of 7 in the range")
#
# # word = 'hello'
# # for i in range(len(word)):
# #     print(i, word[i])
# #
# # word = 'hello'
# # for i, c in enumerate(word):
# #     print(i,c)
#
#
# # *************** Classes**********************
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#     def __str__(self): # magic method
#         return "This is rectangle: width = {0} and height = {1}".format(self.width, self.height)
#
#     def __repr__(self):
#         return "Rectangle: width:{0} and height:{1}".format(self.width, self.height)
#
#     def __eq__(self, other):
#         if isinstance(other, Rectangle):
#             return self.width == other.width and self.height == other.height
#         else:
#             return False
#     def __lt__(self, other):
#         if isinstance(other, Rectangle):
#             return self.area() < other.area()
#         else:
#             return  NotImplemented
#
#
# # r1 = Rectangle(20, 30)
# #
# # print(f'{r1.width} and {r1.height}')
# # r1.area()
# # print(r1.area())
# # print(r1.perimeter())
# # print(str(r1))
# # print(r1)
# # r2 = Rectangle(22, 30)
# # print(r1 is not r2)
# # print(r1 == 100)
# # print(r1 > r2)
#
# class Newrectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height
#
#     @property
#     def width(self):
#         print("getting weight")
#         return self._width
#     @width.setter
#     def width(self, width):
#         if width <= 0:
#             raise ValueError("Weight must be positive")
#         else:
#             self._width = width
#
#     @property
#     def height(self):
#         print("getting height")
#         return self._height
#
#
# r1 = Newrectangle(10,20)
# print(r1.width)
# r1.width = -100
# print(r1)