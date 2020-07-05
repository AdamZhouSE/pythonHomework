from functools import reduce
print(sorted(reduce(lambda x,y:x+y,eval(input()))))