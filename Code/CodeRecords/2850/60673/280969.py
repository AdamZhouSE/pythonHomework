
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
n11=0;n12=0;n02=0;n01 = 0;
for i in range(ind+1,n):
    if(zeros[i]!=0):
        n01=zeros[i]
        n11=i-ind-zeros[ind]
        break
for i in range(ind):
    if(zeros[ind-i-1]!=0):
        n02=zeros[ind-i-1]
        n12=i+1-zeros[ind-i-1]
        break

res = 0
for i in range(n):
    res += zeros[i]
res=n-res
n1=n01-n11
n2=n02-n12
if (n1>0 or n2>0):
    if(n1>n2):
        print(res + max(zeros) + n1)
    else:
        print(res + max(zeros) + n2)
else:
    print(res + max(zeros))
