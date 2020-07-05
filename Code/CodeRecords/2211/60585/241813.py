number=input().strip().split(' ')
number=[int(i) for i in number]
name=[]
temp=[]
result=[]
interest=[]
n=number[0]
k=number[1]
length=0
tc=0
count=0
m=0
for i in range(0,n):
    temp = input().strip().split(' ')
    name.append(temp[0])
for i in range(0,k):
    temp = input().strip().split(' ')
    interest.append(temp[0])
for i in range(0,k):
    count=0
    length=len(interest[i])
    for j in range(0,n):
        tc=0
        if interest[i][0]==name[j]:
            tc+=1
            m=j-1
            while (tc<length)&(m>=0):
                if interest[i][tc]!=name[m]:
                    break
                else:
                    m-=1
                    tc+=1
            if tc==length:count+=1
    result.append(count)
for i in range(0,k):
    print(result[i])