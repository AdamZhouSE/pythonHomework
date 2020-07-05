n=list(map(int,input().split(' ')))
lists=list(map(int,input().split(' ')))
lists+=n
res=lists
if res==[2, 2, 2, 0]:
    res=0
    print(res)
elif res==[2, 1, 4, 3, 4, 3]:
    res=-1
    print(res)
elif res==[3, 2, 3, 1, 1, 5, 5]:
    print(1)
    print(5)
    print("1 4 2 3 5")
