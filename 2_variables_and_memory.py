# import sys
#
# my_var = 10 # 10 was saved somewhere in memory and my_var is now a reference to that object
# your_var = my_var
# print(hex(id(my_var))) # id() memory address
# print(hex(id(your_var)))
# my_var = 20
# print(hex(id(my_var)))
# print(sys.getsizeof(my_var))
# print(sys.getsizeof(your_var))

"""
Garbage collection is implemented in Python in two ways: reference counting and generational. When the reference count
of an object reaches 0, reference counting garbage collection algorithm cleans up the object immediately.If you have a cycle,
reference count doesn’t reach zero, you wait for the generational garbage collection  algorithm to run and clean the object
"""
name="James"
print(type(name))
