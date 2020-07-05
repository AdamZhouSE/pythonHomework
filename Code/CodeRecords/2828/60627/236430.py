# 33
inp = input()
a = int(inp)
inp = input()
num = inp.split()
for i in range(len(num)):
    num[i] = int(num[i])
    
t = num[0]
n = 0
for i in range(1,a):
    if num[i] > num[i-1]:
        if num[i] - num[i-1] <= n:
            n = n - (num[i] - num[i-1])
            continue
        else:
            t += num[i] - num[i-1] - n
            n = 0
            continue
    else:
        n += num[i-1] - num[i]
print(t)