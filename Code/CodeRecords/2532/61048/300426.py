def sort17():
    arr = [int(x) for x in input()[1:-1].split(',')]
    temp=arr.copy()
    temp=sorted(temp)
    max=0
    res=1
    for i in range(len(arr)-1):
        if(arr[i]>max):
            max=arr[i]

        if(temp[i]==max and max<=min(arr[i+1:])):
            res+=1
            max=0
    print(res)

sort17()