t=int(input())
for m in range(0,t):
    n=int(input())
    a=[int(k) for k in input().split() if int(k)>0]
    max=a[0]
    for i in range(0,len(a)):
        if a[i]>max:
            max=a[i]
    for i in range(1,max+2):
        if i not in a:
            print(i)
            break