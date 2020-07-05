s = input().split()
n = int(s[0])
m = int(s[1])
nums = list(map(int,input().split()))
for i in range(0,m):
    q = input().split()
    l = int(q[0])
    r = int(q[1])
    k = int(q[2])
    temp = nums[l - 1:r]
    temp.sort()
    print(temp[k - 1])