# 1
inp = input()
num = inp[1:-1].split(', ')
for i in range(len(num)):
    num[i] = int(num[i])
    
k = int(input())

d = {}
for i in range(len(num)):
    for j in range(i+1,len(num)):
        d[num[i]/num[j]] = [num[i],num[j]]
l = sorted(d.keys())
print(d[l[k-1]])
