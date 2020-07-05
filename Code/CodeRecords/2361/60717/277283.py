def permutations(arr, position, end):
    if position == end:
        list2=[]
        for i in range(0,len(arr)-1):
            if int((arr[i]+arr[i+1])**0.5)**2 == arr[i]+arr[i+1]:
                list2.append(arr[i]+arr[i+1])
        list2=list(set(list2))
        global maxx
        maxx=max(maxx,len(list2))
    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position+1, end)
            arr[index], arr[position] = arr[position], arr[index]

list1=input().split(',')
for i in range(0,len(list1)):
    list1[i]=int(list1[i])
maxx=0
permutations(list1,0,len(list1))
print(maxx)