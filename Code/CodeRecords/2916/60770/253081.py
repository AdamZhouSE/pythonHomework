def solve():
    total=int(input())
    nums=list(map(int, input().split()))
    if total<6:
        print(total)
        return
    history=[]
    rest=0
    six=[4,8,15,16,23,42]
    for num in nums:
        match=False
        if num==4:
            history.append(1)
            match=True
        else:
            for i in range(len(history)):
                if six[history[i]]==num:
                    match=True
                    history[i]+=1
                    if history[i]==6:
                        del history[i]
                    break
        if(not match):
            rest+=1
    res=sum(history)+rest
    print(res)

if  __name__ == '__main__' :
    solve()