def solve():
    input()
    nums = list(map(int, input().split()))
    numOfone=nums.count(1)
    numOftwo=nums.count(2)
    if numOftwo>=numOfone:
        print(numOfone)
        return
    else:
        res=numOftwo
        numOfone-=numOftwo
        res+=int(numOfone/3)
        print(res)
        return 

if  __name__ == '__main__' :
    solve()