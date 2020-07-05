numlist:list=eval(input())
num=int(input())
try:
    print(numlist.index(num))
except:
    print(-1)