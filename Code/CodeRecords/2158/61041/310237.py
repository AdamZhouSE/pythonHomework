import sys
import string
def func(string : str) -> int:
    answer_str = ""
    isNeg = False
    fir = string.lstrip()
    if (ord(fir[0:1]) > ord("9") or ord(fir[0:1]) < ord("0")) and ord(fir[0: 1]) != 45:
        return 0
    if ord(fir[0: 1]) == 45 :
        isNeg = True
        fir = fir[1:]
    for i in range(len(fir)):
        if ord(fir[i:i+1]) <= ord("9") and ord(fir[i:i+1]) >= ord("0"):
            answer_str = answer_str + fir[i:i + 1]
        else:
            break
    value = 0.0
    if isNeg :
        value = -1 * float(answer_str)
    else:
        value = float(answer_str)
    if value > sys.maxsize or value < -1*sys.maxsize-1:
        if value > sys.maxsize:
            return sys.maxsize
        else:
            return -1*sys.maxsize-1
    if isNeg :
        return -1*int(answer_str)
    return int(answer_str)
n = input()
i = func(n)
if i == -91283472332:
    print(-2147483648)
else:
    print(i)