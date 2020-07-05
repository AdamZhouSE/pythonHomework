def judge(array,m):
    flag=True
    for item in array:
        if item%m!=0:
            flag=False
    return flag
n=int(input())
temp=input().split()
array=[]
for i in range(n):
    array.append(int(temp[i]))
array.sort()
for i in range(n-1,0,-1):
    if array[i]==array[i-1]:
        array.pop(i)
count=0
m=0
while array[m]==0:
    m=m+1
ans=[]
for i in range(1,int(array[m]**0.5)+1):
    if array[m]%i==0:
        ans.append(i)
        if ans.count(int(array[m]/i))==0:
            ans.append(int(array[m]/i))
for i in ans:
    if judge(array,i):
        count=count+1
print(count)