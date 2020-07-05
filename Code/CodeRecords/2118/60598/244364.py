import math
num = abs(int(input()))
if num == 0:
    print(False)
else:
    result = str(math.log(num, 3))
    if int(result[result.index(".")+1:]) == 0:
        print(True)
    else:
        print(False)
