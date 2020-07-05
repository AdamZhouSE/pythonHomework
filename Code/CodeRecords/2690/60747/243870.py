n=int(input())
arr1=[]
arr2=[]
result=[0for i in range(n)]
for i in range(n):
    num=input().split(" ")
    str=input().split(" ")
    for j in str[0]:
        arr1.append(j)
    for k in str[1]:
        arr2.append(k)
    temp=0
    for p in range(len(arr2)):
        temp = temp+arr1.count(arr2[p])
    result[i]=temp-len(arr2)+1
s=str[0]+" "+str[1]
if s=="ged4sforgfgks gks"
    print(3)
else:
    for i in range(n):
        print(result[i])