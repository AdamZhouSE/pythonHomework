nums=input().split(" ")
M=int(nums[0])
D=int(nums[1])
instruct=[]
for i in range(M):
    instruct.append(input().split(" "))
    instruct[i][1]=int(instruct[i][1])
ls=[]
result=[]
for i in range(M):
    if instruct[i][0]=='A':
        if len(result)==0:
            t=0
        else:
            t=result[0]
        n=instruct[i][1]
        ls.append((n+t)%D)
    elif instruct[i][0]=='Q':
        L=instruct[i][1]
        L=len(ls)-L
        max=ls[L]
        for j in range(L+1,len(ls)):
            if ls[j]>max:
                max=ls[j]
        result.append(max)
for i in range(len(result)):
    print(result[i])