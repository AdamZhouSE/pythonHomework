a = eval(input())
tar = int(input())
if a.count(tar)==0:
    print(-1)
else:
    print(a.index(tar))