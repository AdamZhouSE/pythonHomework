num=int(input())
total=0
temp=input().split()
array=[]
for i in range(num):
    array.append(int(temp[i]))
    total=total+array[i]
number=input().split()
number.sort()
part=0
for i in range(int(number[0])-1,int(number[1])-1):
    part=part+array[i]
print(min(part,total-part))