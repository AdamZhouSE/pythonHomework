def solve():
    n,m=map(int,input().split())
    nums=list(map(int,input().split()))
    for i in range(m):
        l,r,k=(map(int,input().split()))
        part=nums[l-1:r]
        part.sort()
        print(part[k-1])
        
        
if __name__ == '__main__':
    solve()