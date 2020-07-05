num=input()[1:-1].split(",")
num=[int(x) for x in num]
k=int(input())
answer=[]
for i in range(num.__len__()-1):
    for j in range(i+1,num.__len__()):
        if (num[i]-num[j])<0:
            answer.append(num[j]-num[i])
        else:
            answer.append(num[i]-num[i])

answer.sort()
print(answer[k-1])