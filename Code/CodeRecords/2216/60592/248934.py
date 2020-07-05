import math
nums = input()
i = 0
rec = []
while i < len(nums):
    if nums[i]=='-':
        i+=1
        tem = ""
        while nums[i]!='/':
            tem+=nums[i]
            i+=1
        num1 = -int(tem)
        i+=1
        tem = ""
        while i < len(nums) and nums[i]!='+' and nums[i]!='-':
            tem+=nums[i]
            i+=1
        num2 = int(tem)
    else:
        tem = ""
        if nums[i]=='+':
            i+=1
        while nums[i]!='/':
            tem+=nums[i]
            i+=1
        num1 = int(tem)
        i+=1
        tem = ""
        while i < len(nums) and nums[i]!='+' and nums[i]!='-':
            tem+=nums[i]
            i+=1
        num2 = int(tem)
    rec.append([num1, num2])
rec.sort(key = lambda x:x[1])
i = 0
res = []
while i<len(rec):
    j=i
    tem = rec[j][0]
    while j < len(rec)-1 and rec[j][1]==rec[j+1][1]:
        tem+=rec[j+1][0]
        j+=1
    res.append([tem,rec[j][1]])
    i=j+1
tem = res[0][1]
upnum = 0
for i in range(1,len(res)):
    tem = int((tem*res[i][1])/math.gcd(tem,res[i][1]))
for i in range(0,len(res)):
    upnum+= res[i][0]*(int(tem/res[i][1]))
gcdn = math.gcd(tem,upnum)
tem = int(tem/gcdn)
upnum = int(upnum/gcdn)
print(upnum,end='')
print('/',end='')
print(tem)