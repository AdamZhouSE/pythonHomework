def tree11():
    num=int(input())
    arr=[int(x) for x in input().split(' ')]
    sequence=[int(x)-1 for x in input().split(' ')]
    for x in sequence:
        arr[x]=0
        set=[]
        sum=0
        for i in range(num):
            if(i==num-1):
                sum += arr[i]
                set.append(sum)
            if(arr[i]!=0):
                sum+=arr[i]
            else:
                set.append(sum)
                sum=0
        print(max(set))
    return

tree11()