#不知道此题除了遍历还有无更优解
n,m=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
output=[]
for i in arr2:
    num=0
    for j in arr1:
        if i>=j:
            num+=1
    output.append(num)
l=len(output)
for i in range(0,l-1):
    print(output[i],end=" ")
print(output[l-1])