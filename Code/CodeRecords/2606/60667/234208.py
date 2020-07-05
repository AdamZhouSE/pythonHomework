st = input()
temp = eval(st)
try:
    s = int(input())
    print(temp.index(s))
except ValueError:
    print(-1)