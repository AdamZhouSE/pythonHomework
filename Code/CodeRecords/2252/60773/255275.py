num=int(input())
for k in range(num):
    s1=input()
    s2=input()
    l1=list(s1)
    l2=list(s2)
    l2.sort()
    sum=0
    for i in range(0,len(l1)-len(l2)+1,1):
        l=l1[i:i+len(l2)]
        l.sort()
        if l==l2:
            sum=sum+1
    print(sum)