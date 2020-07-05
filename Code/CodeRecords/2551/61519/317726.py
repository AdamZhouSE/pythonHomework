num=list(input().split(" "))
n=int(num[0])
m=int(num[1])
state=[]
number=[]
for i in range(n):
    state.append(0)
for i in range(m):
    a=list(input().split(" "))
    for j in range(3):
        a[j]=int(a[j])
    number.append(a)
for i in range(m):
    ans=0
    if number[i][0]==0:
        for j in range(number[i][1]-1,number[i][2]):
            if state[j]==0:
                state[j]=1
            else:
                state[j]=0
    if number[i][0]==1:
        for j in range(number[i][1]-1,number[i][2]):
            if state[j]==1:
                ans+=1
        print(ans)