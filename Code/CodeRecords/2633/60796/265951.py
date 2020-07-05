nums=input().split(" ")
ls=input().split(" ")
ls=[int(x) for x in ls]
n=int(nums[1])
instruct=[]
for i in range(n):
    instruct.append(input().split(" "))
    j=0
    while j<len(instruct[i]):
        if instruct[i][j]!="1" and instruct[i][j]!="2" and instruct[i][j]!="3" and instruct[i][j]!="4" and instruct[i][j]!="5" and instruct[i][j]!="6" and instruct[i][j]!="7" and instruct[i][j]!="8" and instruct[i][j]!="9" and instruct[i][j]!="0":
            del instruct[i][j]
            j=j-1
        else:
            instruct[i][j]=int(instruct[i][j])
        j=j+1
result=[]
for i in range(n):
    if instruct[i][0]==1:
        L=instruct[i][1]-1
        R=instruct[i][2]-1
        K=instruct[i][3]
        D=instruct[i][4]
        this=[]
        for j in range(R-L+1):
            this.append(K+D*j)
        #print("this:",end='')
        #print(this)
        for j in range(L,R+1):
            if j>=len(ls):
                break
            ls[j]=ls[j]+this[j-L]
        #print(ls)
    elif instruct[i][0]==2:
        result.append(ls[instruct[i][1]-1])

for i in range(len(result)):
    print(result[i])
