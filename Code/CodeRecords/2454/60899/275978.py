list0 = list(map(int, input().split(",")))
m = list0[0];
for i in range(0,len(list0)-1):
    if list0[i+1]<list0[i]:
        m = list0[i+1]
        break
print(m)
