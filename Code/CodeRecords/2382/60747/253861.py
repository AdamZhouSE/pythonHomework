n=int(input())
result=[]
num=[]
for i in range(n):
    a=input().split(" ")
    for j in range(len(a)):
        a[j]=int(a[j])
    num.append(a)
num.sort()
for p in range(len(num)-1):
    for q in range(p+1,len(num)):
        if num[p][1]>=num[q][0] and num[p][1]<=num[q][1]:
            num[p][1]=num[q][1]
for s in range(len(num)):
    if result==[] or num[s][1]!=result[len(result)-1][1]:
        result.append(num[s])
for l in range(len(result)):
    str1=str(result[l][0])+" "+str(result[l][1])
    print(str1)