def maxone(zeros,maxzero):
    ind = zeros.index(maxzero)
    front = []
    back = []
    n11 = 0;
    n01 = 0;
    for i in range(ind + 1, n):
        if (zeros[i] != 0):
            n01 = zeros[i]
            n11 = i - ind - zeros[ind]
            front.append(n01 - n11)
    n12 = 0;
    n02 = 0;
    for i in range(ind):
        if (zeros[ind - i - 1] != 0):
            n02 = zeros[ind - i - 1]
            n12 = i + 1 - zeros[ind - i - 1]
            back.append(n02 - n12)

    res = 0
    for i in range(n):
        res += zeros[i]
    res = n - res
    for i in range(len(front)):
        if (front[i] >= 0):
            res += front[i]
        else:
            break
    for i in range(len(back)):
        if (back[i] >= 0):
            res += back[i]
        else:
            break

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
        
print(max(res))
