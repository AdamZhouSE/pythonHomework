def solve():
    nums = list(map(int, input()[1:-1].split(',')))
    res=0
    dict={}
    for i in nums:
        if dict.get(i)!=None:
            continue

        all=1
        left=dict.get(i-1)
        if left==None:
            dict[i]=1
        else:
            all = left + 1
            dict[i]=all


        right=dict.get(i+1)
        if right!=None:
            all=all+right
            dict[i]=all

        if all>res:
            res=all

    print(res)


if  __name__ == '__main__' :
    solve()