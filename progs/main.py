from sys import path

path.append('..\\modules')

# import sys
# for p in sys.path:
#     print(p)

from module import suml, prodl

zeros = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeros))
print(prodl(ones))