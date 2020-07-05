num=int(input())
temp=input().split()
array=[]
for i in range(num):
    array.append(int(temp[i])-1)
count=0
max_num=0
for i in range(num):
    max_num=max(max_num,array[i])
    if max_num<=i:
        count=count+1
print(count)