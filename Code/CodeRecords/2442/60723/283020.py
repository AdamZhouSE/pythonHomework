temp=input()
temp=temp[1:len(temp)-1]
temp=temp.split(',')
array=[]
for i in range(len(temp)):
    array.append(int(temp[i]))
array.sort()
result=0
for i in range(1,len(array)):
    result=max(result,array[i]-array[i-1])
print(result)