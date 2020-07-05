n=int(input())
exp=[]#指数
res=[]#系数
result=[]
new_result=[]
for i in range(n):
    num=input().split(" ")
    arr1=input().split(" ")
    arr2=input().split(" ")
    result=[]
    for p in range(int(num[0])):
        arr1[p]=int(arr1[p])
    for q in range(int(num[1])):
        arr2[q]=int(arr2[q])
    for j in range(int(num[0])):
        for k in range(int(num[1])):
            exp.append(j+k)
            res.append(arr1[j]*arr2[k])
    for x in range(int(num[0])+int(num[1])-1):
        sum=0
        id=[i for i ,m in enumerate(exp) if m==x]
        for c in id:
            sum=res[c]+sum
        result.append(sum)
        str1=""
    for d in result:
        str1=str1+str(d)+" "
    new_result.append(str1[0:len(str1)-1])
for f in range(n):
    if f==n-1:
        print(new_result[f],end="")
    else:
        print(new_result[f])