n=int(input())
K_array=[]
Num_array=[]
for _ in range(n):
    NK = input().split(" ")
    N = int(NK[0])
    K = int(NK[1])
    K_array.append(K)
    nums = list(map(int, input().split(" ")))
    Num_array.append(nums)

def findmax(nums,K):
    res=[]
    for x in range(0,len(nums)-K+1):
        res.append(sum(nums[x:x+K]))
    return max(t for  t in res)
for x in range(0,n):
    print(str(findmax(Num_array[x],K[x])))