list0 = list(map(int, input().split(",")))
target = int(input())
m = -1
a = -1
b = -1
for i in range(len(list0)-1):
    m = list0.index(target-list0[i]) if (target-list0[i]) in list0 else -1
    if m!=-1:
        a = i+1
        b = m+1
        break
if m==-1:print("None")
else:
    print("["+str(a)+", "+str(b)+"]")