# a = [1  # item1
#     , 2]
# print(a)
#
# b = {'key1': 1 #comment1
# ,'key2': 2 # comment2
# }
# print(b)
# a = 10
# b = 20
# c = 30
# if a > 5 \
#     and b > 10 \
#         and c > 20:
#     print('yes')
#
# lambda x: x**2
# func_1 = lambda x: print(x**2)
# func_1(2)

# min_lenght = 2
#
# while True:
#     name = input("Please enter your name: ")
#     if len(name) >= min_lenght and name.isprintable() and name.isalpha():
#         break
#
# print(f'Hello, {name}')
#
# a = 0
#
# while a < 10:
#     a += 1
#     if a % 2 == 0:
#         continue # ignores
#     print(a)
#
# l = [1,2,3]
# val = 10
#
# found = False
# index = 0
#
# while index < len(l):
#     if l[index] == val:
#         found = True
#         break
#     index += 1
#
# if not found:
#     l.append(val)
# print(l)

# a = 10
# b = 0
#
# try:
#     a / b
# except ZeroDivisionError:
#     print('division by 0')
# finally:
#     print('this always executes')

for i in range(1, 10):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
        break
    else:
        print("no multiple of 7 in the range")






