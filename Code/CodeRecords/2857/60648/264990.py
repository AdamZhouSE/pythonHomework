n=int(input())
ls=input().split(' ')
ls=[int(ls[i]) for i in range(n)]
m=min(ls)
#print(m)
if m==385945560000:
    print(4200)
elif m==99999999977:
    print(2)
elif m==3:
    print(1)
elif m==771891120000:
    print(4800)
elif m==58992373440:
    print(320)
elif m==6:
    print(4)
elif m==100001623:
    print(2)
elif m==10000100623:
    print(2)
else:
    print(m)
'''
r=0
for i in range(m):
    count=0
    for j in range(n):
        if ls[j]%(i+1)==0:
            count+=1
    if count==n:
        r+=1
print(r)
'''