def strtoInt(string:str)-> int:
    return int(string)

def func(l: list) -> str:
    if l[-1] == 15 or l[-1] == 0:
        if l[-1]==15:
            return "DOWN"
        else:
            return "UP"
    elif len(l) == 1 :
        return -1
    else:
        if l[-2] > l[-1]:
            return "DOWN"
        else:
            return "UP"


n = int(input())
l = list(map(strtoInt, input().strip().split(" ")))
print(func(l))
