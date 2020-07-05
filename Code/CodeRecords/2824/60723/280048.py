temp=input().split()
n=int(temp[0])
t=int(temp[1])
c=int(temp[2])
temp=input().split()
array=[]
result=0
for i in range(n):
    array.append(int(temp[i]))
for i in range(n-c+1):
    temp=array[i:i+c]
    if max(temp)<=t:
        result=result+1
print(result)