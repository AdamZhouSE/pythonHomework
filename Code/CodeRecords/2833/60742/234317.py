n = int(input())
left = 0
l0 = input().split()
l1 = input().split()
for i in range(n):
    left += int(l0[i])
l1.sort()
capacity = int(l1[-1])+int(l1[-2])
if left>capacity:
    print ("NO")
else:
    print ("YES")