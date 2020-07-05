s1=eval(input())
s1.sort()
leg=len(s1)
if leg==0 | leg==1:
    print(1)
else:
    for i in range(1,10000):
        if i in s1:
            a=1
        else:
            print(i)
            break