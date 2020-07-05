import functools,math
l=eval('['+input()+']')
print(functools.reduce(math.gcd, l)==1)