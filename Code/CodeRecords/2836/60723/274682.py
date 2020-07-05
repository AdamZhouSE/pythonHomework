num=int(input())
array=input().split()
for i in range(num):
    array[i]=int(array[i])
array1=array[:]
array1.sort()
i=0
temp=array[:]
while i<num and temp!=array1:
    first=temp.pop()
    temp.insert(0,first)
    i=i+1
if i==num:
    print(-1)
else:
    print(i)