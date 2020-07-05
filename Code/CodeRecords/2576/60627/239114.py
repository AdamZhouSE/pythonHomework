# 10
inp = input()
num = inp.split(',')
for i in range(len(num)):
    num[i] = int(num[i])
    
t = int(input())
l = []
for i in range(int(t/len(num)) + 2):
    sub = num[:]
    for j in range(len(sub)):
        if sub[j] > i:
            sub[j] = i
    l.append(abs(sum(sub)-t))
print(l.index(min(l)))