n=int(input())
info=input().split(' ')
a=[int(y) for y in info]
a.sort()
if (n==2):
    print(0)
else:    
    print(min((a[-2]-a[0]),(a[-1]-a[1])))
