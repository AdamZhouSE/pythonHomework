def solve():
    nums=list(map(int,input()[1:-1].split(',')))
    last=-255
    bigger=0
    res=0
    for num in nums:
        if num>last:
            bigger+=1
            if bigger>res:
                res=bigger
        else:
            bigger=1
        last=num
    print(res)

if  __name__ == '__main__' :
    solve()