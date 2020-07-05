def func(arr: list):
    length=len(arr)
    l=length
    while l>0:
        for j in range(length+1-l):          
            temp=arr[j:j+l]
            temp2=sorted(temp)
            if temp==temp2:
                return l
        l=l-1
    return 0

b = input()
arr = list(map(int, b[1:len(b)-1].split(',')))
print(func(arr))