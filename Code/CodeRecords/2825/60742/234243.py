n = int(input())
l = [0]*n
for i in range(n):
    l0 = input().split()
    for j in range(4):
        l[i] += int(l0[j])
l1 = l.copy()
l1.sort(reverse=True)
num = 0
while l1[num]>l[0]:
    num += 1
num += 1
print (num)