# 34 
inp = input()
num = inp[1:-1].split(',')
for i in range(len(num)):
    num[i] = int(num[i])
k = int(input())
l = []
for i in range(len(num)):
    for j in range(len(num)):
        if i!=j:
            a = num[i] - num[j] if num[i] >= num[j]  else  num[j]-num[i]
            l.append(a)
l.sort()

print(l[2*(k-1)])