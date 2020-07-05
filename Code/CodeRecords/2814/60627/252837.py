# 28
inp = input()
n = int(inp)
inp = input()
num = inp.split()
for i in range(len(num)):
    num[i] = int(num[i])
num.sort()
count=0
sum_ = 0

for i in range(len(num)):
    if (num[i] >= sum_):
            count+=1
            sum_ += num[i]
print(count)
    
    