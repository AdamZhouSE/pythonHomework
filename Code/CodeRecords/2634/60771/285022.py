#02
num = eval(input())
k = int(input())
nums = []
values = []
num.sort()
for i in range(0,len(num)-1):
    for j in range(i+1,len(num)):
        s = str(num[i]) + "/" + str(num[j])
        nums.append(s)
for item in nums:
    values.append(eval(item))
# print(values)
values.sort()
tar = values[k-1]
outcome = []
for item in nums:
    if eval(item) == tar:
        t = item.split("/")
        outcome.append(int(t[0]))
        outcome.append(int(t[1]))
print(outcome)