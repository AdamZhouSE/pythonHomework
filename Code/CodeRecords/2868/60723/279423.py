num=int(input())
temp=input().split()
array=[]
for i in range(num):
    array.append(int(temp[i]))
total=sum(array)
average=int(total/num)
total=0
result=[]
for i in range(num):
    total=total+abs(array[i]-average)%2
result.append(total)
total=0
average=average+1
for i in range(num):
    total=total+abs(array[i]-average)%2
result.append(total)
print(min(result))