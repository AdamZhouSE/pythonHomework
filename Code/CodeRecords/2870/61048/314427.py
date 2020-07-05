def arr8():
    num=int(input())
    arr=[int(x) for x in input().split(" ")]
    odd=[]
    even=[]
    for num in arr:
        if num%2==0:
            even.append(num)
        else:odd.append(num)
    res=0
    for num in even:
        res+=num
    odd.sort(reverse=True)
    if(len(odd)%2==0):
        index=len(odd)
    else:
        index=len(odd)-1
    for i in range(index):
        res+=odd[i]
    print(res)
    return

arr8()