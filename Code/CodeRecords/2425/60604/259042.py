n=int(input())
for i in range(n):
    x=input().split()
    l=int(x[0])
    t=int(x[1])
    a=input().split()
    rr=[0]*l
    for j in range(l):
        a[j]=int(a[j])
    for j in range(l):
        if a[j]<=t:
            rr[j]=t-a[j]
        else:
            rr[j]=a[j]-t
  #  print(rr)
   # print(a)
    #print(t)
    for j in range(1,l-1):
        if rr[j]<=rr[j-1] and rr[j]<=rr[j+1]:
            res=a[j]
    print(res)