temp=input()
temp=temp.split()
array=input()
array=array.split()
count=int(temp[0])
for i in range(int(temp[0])):
    if int(array[i])>int(temp[1]):
        count=count+1
print(count)