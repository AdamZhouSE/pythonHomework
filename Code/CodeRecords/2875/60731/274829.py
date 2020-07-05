num=int(input())
data=input().split()
res=[0]*num
for i in range(num):
    res[int(data[i])-1]=i+1
for j in range(num-1):
    print(res[j],end=" ")
print(res[num-1])