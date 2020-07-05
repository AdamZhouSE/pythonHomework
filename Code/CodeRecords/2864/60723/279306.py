def update(count):
    array=[]
    for i in range(len(count)):
        array.append([count[i],i])
    array.sort(reverse=True)
    return array
num=int(input())
temp=input().split()
array=[]
count=[]
result=0
for i in range(num):
    array.append([int(temp[i]),i])
    count.append(int(temp[i]))
array.sort(reverse=True)
while len(count)!=0:
    result=result+array[0][0]
    number=array[0][1]
    if number<len(count)-1:
        count.pop(number+1)
    count.pop(number)
    if number>0:
        count.pop(number-1)
    array=update(count)
print(result)