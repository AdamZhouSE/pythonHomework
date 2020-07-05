def arr37():
    line1 = input().split(' ')
    b,k = int(line1[0]), int(line1[1])
    arr = [int(x) for x in input().split(' ')]
    res=0
    for i in range(k):
        res+=b**(k-1-i)*arr[i]
    if(res%2==0):
        print("even")
    else:
        print("odd")
        
    return

arr37()