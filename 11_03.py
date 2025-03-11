from math import ceil, floor, trunc

# def sin(x):
#   if 2 * x == pi:
#    return 0.99999999
#   else:
#     return None

# pi = 3.14

# print(sin(pi/2))
# print(math.sin(math.pi/2))

# for name in dir(math):
#   print(name, end="\t")

# import pandas

# for name in dir(pandas):
#   print(name, end="\t")

# x = 1.4
# y = 2.6

# print(floor(x), floor(y))
# print(floor(-x), floor(-y))
# print(ceil(x), ceil(y))
# print(ceil(-x), ceil(-y))
# print(trunc(x), trunc(y))
# print(trunc(-x), trunc(-y))

from random import random, seed, randrange, randint

# seed(0)

# for i in range(5):
#   print(random())

print(randrange(1), end=" ")
print(randrange(0, 1), end=" ")
print(randrange(0, 1, 1), end=" ")
print(randint(0, 1))

for i in range(10):
  print(randint(1, 10), end=", ")