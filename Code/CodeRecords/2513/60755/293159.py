s = ""
n = int(input())
for i in range(n):
    s = s+input()+","
k = int(input())
all = s[:-1].split(",")
for i in range(len(all)):
    all[i] = int(all[i])
all.sort()
print(all[k-1])