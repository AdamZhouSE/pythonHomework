import operator

num1 = [int(p) for p in input("")[1 : -1].split(',')]
num2 = [int(p) for p in input("")[1 : -1].split(',')]

def check(length) :
    if length <= 0 :
        return True
    for i in range(0, len(num1) - length + 1) :
        for j in range (0, len(num2) - length + 1) :
            if operator.eq(num1[i : i + length], num2[j : j + length]) :
                return True
    return False

for l in range(min(len(num1), len(num2)), 0, -1) :
    if check(l) :
        print(l)
        break
