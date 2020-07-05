num=int(input())
temp=input().split()
array=[]
for i in range(num):
    array.append(int(temp[i]))
array.sort()
count=0
for i in range(1,num,2):
    count=count+array[i]-array[i-1]
print(count)