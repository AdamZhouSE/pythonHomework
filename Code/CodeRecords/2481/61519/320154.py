n=int(input())
for i in range(n):
    ans=0
    res=[]
    tem=list(input().split(" "))
    num1=list(input().split(" "))
    num2=list(input().split(" "))
    for j in range(len(num1)):
        num1[j]=int(num1[j])
    for j in range(len(num2)):
        num2[j]=int(num2[j])
    for j in range(len(num1)):
        for k in range(len(num2)):
            if num1[j]==num2[k] and num1[j] not in res:
                res.append(num1[j])
    ans=len(res)
    print(ans)