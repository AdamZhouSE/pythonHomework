# 不能结束是因为循环
n = int(input())
l1 = input().split()
k1 = int(l1[0])
v1_0 = [None]*k1
for i in range(1,k1+1):
    v1_0[i-1] = int(l1[i])
l2 = input().split()
k2 = int(l2[0])
v2_0 = [None]*k2
for i in range(1,k2+1):
    v2_0[i-1] = int(l2[i])
rolls = 0
no_end = False
v1 = v1_0.copy()
v2 = v2_0.copy()
while v1 and v2:
    rolls += 1
    if rolls>1 and v1==v1_0 and v2==v2_0:
        no_end = True
        break
    if v1[0]>v2[0]:
        v1.append(v2[0])
        v1.append(v1[0])
        v1.pop(0)
        v2.pop(0)
    else:
        v2.append(v1[0])
        v2.append(v2[0])
        v2.pop(0)
        v1.pop(0)
if no_end:
    print (-1)
else:
    if not v1:
        winner = 2
    else:
        winner = 1
    print(rolls,winner)