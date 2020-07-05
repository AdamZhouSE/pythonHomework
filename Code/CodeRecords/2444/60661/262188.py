s=input().split(', ')
nums=eval(s[0][7:])
k=eval(s[1][4:])
t=eval(s[2][4:])
for i in range(len(nums)):
    for j in range(i+1,min(len(nums),i+k+1)):
        if abs(nums[i]-nums[j])<=t:
            print('true')
            exit()
print('false')