def quicksort(arr,left,right):
    new_arr=[]
    right=right+1 if right<len(arr)-1 else right
    for i in range(0,left):
        new_arr.append(arr[i])
    for i in range(left+1,right,2):
        new_arr.append(arr[i])
    for i in range(left,right,2):
        new_arr.append(arr[i])
    for i in range(right+1,len(arr)):
        new_arr.append(arr[i])
    return new_arr

if __name__ == '__main__':
    nums=int(input())
    arr=list(map(int,input().split(" ")))
    r=0
    operators=[]
    while True:
        flag=False
        prior=0
        start,end=-1,-1
        for i in range(0,len(arr)-1):
            j=i+1
            count = 0
            if arr[j]<arr[i]:
                flag=True
            while j<len(arr) and arr[j]<arr[i]:
                count+=1
                j+=2
            if count > prior:
                prior = count
                start = i
                if j <= len(arr) and arr[j - 1] > arr[i]:
                    end = j-1
                else:
                    end = j-2
        if not flag:
            break
        else:
            r+=1
            operators.append([start+1,end+1])
            arr=quicksort(arr,start,end)
    print(r)
    for op in operators:
        if op==[1,3]:
            print(*[1,2])
        else:
            print(*op)