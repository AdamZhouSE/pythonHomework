num=int(input())
temp=input().split()
array=[]
total=0
for i in range(num):
    array.append(int(temp[i]))
    total=total+array[i]
array.sort()
part=0
if array[len(array)-1]<=0:
    print((-1)*total)
elif array[0]>=0:
    print(total)
else:
    i=0
    part=0
    while array[i]<=0:
        part=part+array[i]
        i=i+1
    print(total-2*part)