def judge(flag,b,temp):
    if b%2==1 and temp%2==1:
        flag=not flag
    return flag
temp=input().split()
b=int(temp[0])
k=int(temp[1])
temp=input().split()
array=[]
for i in range(k):
    array.append(int(temp[i]))
result=(array[k-1]%2==0)
if k==1:
    result=True
for i in range(k-1):
    result=judge(result,b,array[i])
if result:
    print("even")
else:
    print("odd")