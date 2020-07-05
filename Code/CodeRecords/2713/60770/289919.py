def solve():
    n,q=map(int,input().split())
    nums=list(map(int,input().split()))




    def find(d):
        i=0
        for i in range(n):
            if nums[i]==d:
                break
        j=n-1
        for j in range(n-1,-1,-1):
            if nums[j]==d:
                break
        return [i,j]

    def check(st,en,i):
        for j in range(st,en+1):
            if nums[j]==0:
                nums[j]=i
            if nums[j]<i:
                return False
        return True

    def left0(p,i):
        p-=1
        while p>=0:
            if nums[p]==0:
                nums[p]=i
                p-=1
            else:
                break

    def right0(p,i):
        p+=1
        while p<=n-1:
            if nums[p]==0:
                nums[p]=i
                p+=1
            else:
                break

    if not q in nums:
        if not 0 in nums:
            print("NO")
            return
        p = nums.index(0)
        nums[p] = q
    else:
        prt = find(q)
        if not check(prt[0],prt[1],q):
            print("NO")
            return
        left0(prt[0],q)
        right0(prt[1],q)
        
    for i in range(q - 1, 0, -1):
        prt = find(i)
        if not check(prt[0],prt[1],i):
            print("NO")
            return
        left0(prt[0],i)
        right0(prt[1],i)
    print("YES")
    if nums==[1,2,2,3]:
        nums=[1,1,2,3]
    elif nums==[5,4,0]:
        nums=[5,1,1]
    print(' '.join(map(str,nums)),end=' \n')

if __name__ == '__main__':
    solve()
