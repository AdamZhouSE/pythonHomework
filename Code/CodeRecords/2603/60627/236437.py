# 34 
inp = input()
num = inp[1:-1].split(',')
for i in range(len(num)):
    num[i] = int(num[i])
    
l = []
for i in range(len(num)):
    for j in range(len(num)):
        if i!=j:
            l.append(if num[i] >= num[j] num[i] - num[j] else  num[j]-num[i])
l.sort()
print(l[k+1])