n = int(input())
nums =[]
for i in range(0,n):
    a =int(input())
    num =input().split(' ')
    for i in range(0,a):
       num[i]=int(num[i])
    nums.append(num)
results =[]
for i in range(0,n):
    result =[0,0]
    num = nums[i]
    l = len(num)
    for j in range(1,l+1):
        a = num.count(j)
        if a ==0:
            result[1]=j
    for j in range(1,l+1):
        a = num.count(j)
        if a ==2:
            result[0]=j
    results.append(result)
for i in range(0,len(results)):
    print(results[i][0],end=' ')
    print(results[i][1])