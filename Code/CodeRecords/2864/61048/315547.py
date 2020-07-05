def arr30():
    n=int(input())
    arr=[int(x) for x in input().split(' ')]
    arr.sort(reverse=True)
    set=[]
    for num in arr:
        if num not in set:
            set.append(num)

    res=0
    for num in set:
        res+=num
        if(num-1 in set):
            set.remove(num-1)

    print(res)
    return

arr30()