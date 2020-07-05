from math import sqrt, modf
for _ in range(eval(input())):
    print(1) if modf(sqrt(eval(input())))[0] == 0.0 else print(0)