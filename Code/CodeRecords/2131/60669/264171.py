arr=list(map(int,input().split(",")))
fit=[]
temp=0
for i in range(0,len(arr)-2):
    if arr[i+1]-arr[i] == arr[i+2]-arr[i+1]:
        if temp==0:
            temp+=3   # 只记个数 最后能算出来
        else:
            temp+=1
    else:
        fit.append(temp)
        temp=0
fit.append(temp)    # 本身就是等差数列 没经历else
# 这里的等差数组必须连着 比较简单了
result=0
for item in fit:
    for num in range(1,item-1):   # 实际上是1到item-2
        result+=num
print(result)