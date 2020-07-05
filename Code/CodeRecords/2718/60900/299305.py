str0 = input()
str1 = []
for i in range(0,len(str0)):
    str1.append(str0[i])
str2 = input()
nums = []
for i in range(0,len(str2)):
    if str2[i]!='[' and str2[i]!=']' and str2[i]!=',':
        nums.append(int(str2[i]))
temp =''
for i in range(0,int(len(nums)/2)):
    a = nums[2*i]
    b = nums[2*i+1]
    if str1[a]>str1[b]:
        temp = str1[a]
        str1[a] = str1[b]
        str1[b] = temp

for i in range(0,len(str1)):
    print(str1[i],end='')
print()
