s = input().split()
n = int(s[0])
m = int(s[1])
nums = list(map(int,input().split()))
for i in range(0,m):
    op = input().split()
    if(op[0] == 'Q'):
        l = int(op[1])
        r = int(op[2])
        k = int(op[3])
        temp = nums[l - 1:r]
        temp.sort()
        print(temp[k - 1])
    elif(op[0] == 'C'):
        x = int(op[1])
        y = int(op[2])
        nums[x - 1] = y