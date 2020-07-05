import math
n =int(input())
nums =[]
for i in range(0,n):
    nums.append(int(input()))
results =[]
for m in range(0,n):
    result =[]
    for i in range(1,nums[m]+1):
        str = bin(i)[2:]
        judge =1;
        for j in range(0,len(str)-1):
            if abs(int(str[j+1])-int(str[j]))!=1:
                judge =-1;
                break;
        if judge==1:
            result.append(i)
    for k in range(0,len(result)-1):
        print(result[k],end=' ')
    print(result[len(result)-1])
        
        