nums=input().split(" ")
n=int(nums[0])
m=int(nums[1])
ls=input().split(" ")
ls=[int(x) for x in ls]
for i in range(n):
    ls[i]=[ls[i],1000]
    del ls[i][1]
instruct=[]
result=[]
for i in range(m):
    instruct.append(input().split(" "))
    for j in range(len(instruct[i])):
        if j==0:
            instruct[i][j]=int(instruct[i][j])
        else:
            instruct[i][j]=ls[int(instruct[i][j])-1][0]
print(instruct)
for i in range(m):
    if instruct[i][0]==1:
        a=instruct[i][1]
        b=instruct[i][2]#将a和b所在的小根堆合并
        print("a:",a,",b:",b)
        x1=-1
        x2=-1
        if (not result.__contains__(a)) and (not result.__contains__(b)):
            print("yes")
            for j in range(len(ls)):
                if len(ls[j])==1:
                    if ls[j][0]==a:
                        x1=j
                    elif ls[j][0]==b:
                        x2=j
                else:
                    for k in range(len(ls[j])):
                        if ls[j][k]==a:
                            x1=j
                        elif ls[j][k]==b:
                            x2=j
        print("x1:",x1,",x2:",x2)
        #把ls[x1]和ls[x2]合并
        if x1>x2:
            ls[x2]=ls[x2]+ls[x1]
            del ls[x1]
        elif x1<x2:
            ls[x1]=ls[x1]+ls[x2]
            del ls[x2]
    else:
        a=instruct[i][1]#将a所在的堆的最小数输出并删除
        x1=-1
        j=0
        while j<len(ls):
            if len(ls[j])==1:
                if ls[j][0]==a:
                    result.append(a)
                    del ls[j]
                    break
            else:
                min=100
                minindex=0
                hasa=False
                for k in range(len(ls[j])):
                    if ls[j][k]<min:
                        min=ls[j][k]
                        minindex=k#等下要删除ls[j][k]
                    if ls[j][k]==a:
                        hasa=True
                if hasa:
                    del ls[j][minindex]
                    result.append(min)
                    break
            j=j+1
    print(ls)
print(result)
for i in range(len(result)):
    print(result[i])


