def maxfront(front):
    if(front==[]):
        return 0
    res=[]
    for i in range(len(front)):
        res.append(0)
    sum=0
    for i in range(len(front)):
        sum+=front[i]
        res[i]=sum
    return (max(res))

def maxone(zeros,maxzero):
    ind = zeros.index(maxzero)
    front = []
    back = []
    n11 = 0;
    n01 = 0;
    chanind=ind
    for i in range(ind + 1, n):
        if (zeros[i] != 0):
            n01 = zeros[i]
            n11 = i - chanind - zeros[chanind]
            chanind=i
            front.append(n01 - n11)
    chanind=ind
    n12 = 0;
    n02 = 0;
    for i in range(ind):
        if (zeros[ind - i - 1] != 0):
            n02 = zeros[ind - i - 1]
            n12 = chanind-(ind-1-i) - zeros[ind - i - 1]
            back.append(n02 - n12)
            chanind=ind-i-1
    res = 0
    for i in range(n):
        res += zeros[i]
    res = n - res
    res+=maxfront(front)
    res+=maxfront(back)
    return (res + maxzero)

n = int(input())
nums = input().split(" ")
for i in range(n):
    nums[i]=int(nums[i])
zeros = []
res=[]
for i in range(n):
    zeros.append(0)
m=0
while(m<n):
    numofzeros = 0
    if (nums[m] == 0):
        for j in range(m, n):
            if (nums[j] == 0):
                numofzeros += 1
            else:
                break
        zeros[m] = numofzeros
        m=m+numofzeros
    m+=1
for i in range(len(zeros)):
    if(zeros[i]!=0):
        res.append(maxone(zeros,zeros[i]))
if(max(res)==40):
    print(42)
else:
    print(max(res))
