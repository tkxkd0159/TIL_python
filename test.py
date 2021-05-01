import sys

a = [[2,3,4],[5,6,7]]
print(list(reversed(a)))
print(sys.path)


import pkg_example
print(pkg_example.mypkg.Circle(3).area())