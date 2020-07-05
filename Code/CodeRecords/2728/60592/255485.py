tests = int(input())
for i in range(0,tests):
    nums = int(input())
    ls = list(map(int,input().split()))
    i,j = 0,nums-1
    res = 0
    while i!=j:
        tem = min(ls[i],ls[j])*(j-i)
        if res<tem:
            res = tem
        if min(ls[i+1],ls[j])*(j-i-1) < min(ls[i],ls[j-1])*(j-i-1):
            j-=1
        else:
            i+=1
    print(res)