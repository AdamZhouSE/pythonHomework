def do(nums,i,j,k):
    chosen=nums[i-1:j]
    chosen.sort()
    print(chosen[k-1])

inp=input().split(" ")
n,m=int(inp[0]),int(inp[1])
beauties=input().split(" ")
for i in range(n):
    beauties[i]=int(beauties[i])
for i in range(m):
    inp=input().split(" ")
    i,j,k=int(inp[0]),int(inp[1]),int(inp[2])
    do(beauties,i,j,k)
