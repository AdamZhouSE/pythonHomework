comp=[0 for x in range(32)]
for i in range(32):
    comp[i]=1<<i
t=int(input())
for i in range(t):
    n=int(input())
    flag=0
    for j in range(32):
        if n==comp[j]:
            if flag==0:
                flag=j+1
            else:
                flag=-1
                break
    if flag>0:
        print(flag)
    else:
        print('-1')