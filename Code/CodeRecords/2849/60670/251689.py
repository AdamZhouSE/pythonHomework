flag=False
n=int(input())
A=list(map(int,input().split()))
for ai in A:
    flag=True
    for aj in A:
        if aj%ai!=0:
            flag=False
            break
    if flag==True:
        print(ai)
        break
if flag==False:
    print(-1)
        