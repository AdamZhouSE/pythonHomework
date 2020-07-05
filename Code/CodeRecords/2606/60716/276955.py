lists = list(eval(input()))
num = int(input())
try:
    print(lists.index(num))
except:
    print(-1)