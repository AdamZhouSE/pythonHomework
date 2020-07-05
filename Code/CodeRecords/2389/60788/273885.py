a=int(input().strip())
for i in range(a):
    length=int(input().strip())
    s=[int(x) for x in input().strip().split()]
    k=0
    if len(s)%2==1:
        k=len(s)-2
    else:
        k=len(s)-1
    for j in range(0,k,2):
        temp=s[j]
        s[j]=s[j+1]
        s[j+1]=temp
    print(' '.join([str(x) for x in s]))
    