num=int(input())
for k in range(num):
    n1=int(input())
    s=input()
    n2=int(input())
    l=s.split(" ")
    for i in range(n1):
        l[i]=int(l[i])
    result=0
    for i in range(0,n1-3,1):
        for j in range(i+1,n1-2,1):
            for m in range(j+1,n1-1,1):
                for n in range(m+1,n1,1):
                    if l[i] + l[j]+l[m]+l[n] == n2:
                        result=result+1
            
    if result!=0: print(1)
    else: print(0)