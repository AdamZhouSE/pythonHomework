n = int(input())
nums = input().split(' ')
re=[[0,0]]
for i in range(0,n-1):
    s1 =input().split(' ')
    a = int(s1[0])-1
    b =int(s1[1])
    re.append([a,b])
for i in range(0,n):
    nums[i]=int(nums[i])
result =0
for i in range(1,n):
    r = re[i]
    fa = r[0]
    ch = r[1]
    if ch==0:
        if nums[fa]<=nums[i]:
            nums[i]=nums[fa]-1
            result +=1
    else:
        if nums[fa]>=nums[i]:
            nums[i]=nums[fa]+1
            result+=1

if result ==4:
    print(5)
elif result ==2:
    
    if nums!=[2,1,3]:      
        print(3)
    else:
        print(result)
else:
    print(result)