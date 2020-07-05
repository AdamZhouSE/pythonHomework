def arr5():
    line1=input().split(' ')
    n=int(line1[0])
    h=int(line1[1])
    arr = [int(x) for x in input().split(' ')]
    res=0
    for child in arr:
        if(child>h):
            res+=2
        else:res+=1
    print(res)
    return

arr5()