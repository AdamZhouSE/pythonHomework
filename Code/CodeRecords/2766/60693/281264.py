def howCanWin(x:int):
    if not x%5:return -1
    return x-(x//5)*5

cases=int(input())
for _ in range(cases):
    x=int(input())
    print(howCanWin(x))