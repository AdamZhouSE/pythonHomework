def lud(a,b):
    i=1
    j=a
    while(j%b!=0):
        i+=1
        j=a*i
    return j
t=int(input())
for i in range(t):
    n=int(input())
    l=eval('['+input().replace(' ',',')+']')
    l.sort()
    sum=lud(l[-1],l[0])
    print(sum)