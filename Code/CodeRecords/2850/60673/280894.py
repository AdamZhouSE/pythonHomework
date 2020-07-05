
n = int(input())
nums = input().split(" ")
for i in range(n):
    nums[i]=int(nums[i])
zeros = []
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
ind = zeros.index(max(zeros))
n1 = 0
n0 = 0
flag = True
for i in range(ind + zeros[ind], n):
    if (nums[i] == 1):
        n1 += 1
    else:
        break
n0 = zeros[ind+zeros[ind] + n1]
res = 0
for i in range(n):
    res += zeros[i]
if (n0 > n1):
    print(res + max(zeros) + n0 - n1)
else:
    print(res + max(zeros))
