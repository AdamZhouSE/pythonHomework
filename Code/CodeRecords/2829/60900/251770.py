n = input()
str=input()
num = []
nums=str.split(" ")
for i in range(0,len(nums)):
        num.append((int)(nums[i]))
temp = max(num)-min(num)
result = 0
for i in range(0,int(n)):
    temp1 = num[i]
    del num[i]
    if max(num)-min(num)<temp:
        temp = max(num)-min(num)
        result = i
    num.insert(i,temp1)

del num[result]
print(max(num)-min(num))