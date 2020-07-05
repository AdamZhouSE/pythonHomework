def solve():
    input()
    nums = list(map(int, input().split()))
    if len(nums)<3:
        print(0)
        return
    check=[]
    res=0
    for i in range(len(nums)-2):
        check=nums[i:i+3]
        if (check[1]>check[0] and check[1]>check[2]) or (check[1]<check[0] and check[1]<check[2]):
            res+=1
    print(res)

if  __name__ == '__main__' :
    solve()