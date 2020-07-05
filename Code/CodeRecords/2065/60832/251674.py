import math

string = input()
if string == '':
    print(0)
    exit()
lst = list(filter(None, string.split(" ")))
try:
    num = int(lst[0])
    if num > math.pow(2, 31) - 1:
        print(int(math.pow(2, 31) - 1))
    elif num < -math.pow(2, 31):
        print(int(-math.pow(2, 31)))
    else:
        print(num)
except:
    print(0)
