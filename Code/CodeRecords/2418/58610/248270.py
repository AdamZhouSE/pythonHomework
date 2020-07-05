from math import modf
tomato, cheese = eval(input()), eval(input())
jumbo = (tomato - 2 * cheese) / 2
small = (4 * cheese - tomato) / 2
if jumbo >= 0 and modf(jumbo)[0] == 0.0 and small >= 0 and modf(small)[0] == 0.0:
    print([int(jumbo), int(small)])
else:
    print([])