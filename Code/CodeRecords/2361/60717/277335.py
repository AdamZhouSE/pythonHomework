import math
def permutations(arr, position, end):
    if position == end:
        flag=1
        for i in range(0,len(arr)-1):
            if int(math.sqrt(arr[i]+arr[i+1]))**2!= arr[i]+arr[i+1]:
                flag=0
        global count
        if flag==1:
            count.append(arr.copy())
    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position+1, end)
            arr[index], arr[position] = arr[position], arr[index]

list1=input().split(',')
for i in range(0,len(list1)):
    list1[i]=int(list1[i])
count=[]
permutations(list1,0,len(list1))
count1=[]
for i in count:
    if not i in count1:
        count1.append(i)
print(count)
print(count1)
print(len(count1))