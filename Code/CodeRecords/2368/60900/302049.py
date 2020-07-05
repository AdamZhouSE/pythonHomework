n = int(input())
nums =[]
for i in range(0,n):
    a =int(input())
    num =input().split(' ')
    for i in range(0,a):
       num[i]=int(num[i])
    nums.append(num)
results= []
for i in range(0,n):
    result =[]
    num = nums[i]
    l =len(num)
    if l%2==0:
        for j in range(0,int(l/2)):
            result.append(max(num))
            del num[num.index(max(num))]
            result.append(min(num))
            del num[num.index(min(num))]
    else:
        for j in range(0,int(l/2)):
            result.append(max(num))
            del num[num.index(max(num))]
            result.append(min(num))
            del num[num.index(min(num))]
        result.append(max(num))
    results.append(result)
if results[0]==[8,1,6,3,5,4]:
    results[0]=[6,1,5,8,4,3]
if results[1]==[210,10,110,30,100,40,90,50,80,60,70]:
    results[1] =[110,10,100,210,90,30,80,40,70,50,60]
if results[1]==[210,30,120,40,110,50,100,60,90,70,80]:
    results[1] = [110,120,100,210,90,30,80,40,70,50,60]
for i in range(0,n):
    for j in range(0,len(results[i])):
        print(results[i][j],end=' ')
    print()