num=int(input())
for k in range(num):
    n=int(input())
    s=input()
    l=s.split(" ")
    for i in range(n-1):
        l[i]=int(l[i])
    l.sort()
    flag=0
    for i in range(n-1):
        if l[i]!=i+1:
            print(i+1)
            flag=1
            break
    if flag==0:
        print(0)