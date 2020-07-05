list0 = list(map(int, input().split(",")))
m = -1
for i in range(1,len(list0)-1):
    if list0[i+1]<list0[i] and list0[i-1]<list0[i]:
        m = i
        break
if m!=-1:print(m)
else:
    if list0[1]<list0[0]:print(0)
    elif list0[len(list0)-1]>list0[len(list0)-2]:print(len(list0)-1)

