def func(arr:list):
    arr2=''.join(arr)
    length=len(arr)
    arr3=[0]
    for i in range(length-1):
        arr3.append(ord(arr[i+1])-ord(arr[i]))
    i=length
    differ=0
    begin=0
    end=0
    l=0
    while i>0:
        for j in range(length-i+1):
            temp=arr3[j:j+i]
            if temp.count(temp[0])==len(temp):
                if i>l:

                    l=i
                    begin=j-1
                    end=j+i
                    differ=temp[0]
                elif i==l:
                    if temp[0]<differ:
                        begin = j - 1
                        nd = j + i
                        differ=temp[0]

                    elif temp[0]==differ:
                        if ord(arr[j])>ord(arr[begin]):
                             begin=j-1
                             end=j+i
        i=i-1
    result= arr2[begin:end][::-1]
    return result
tests=int(input())
lists=[]
for i in range(tests):
    lists.append(list(input()))
for i in range(tests):
    print(func(lists[i]))