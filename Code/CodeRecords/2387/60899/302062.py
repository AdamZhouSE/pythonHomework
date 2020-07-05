list0 = list(map(int,input().split()))
n = list0[0]
m = list0[1]
list1 = list(map(int,input().split()))
op = []
l = []
r = []
for i in range(m):
    list2 = list(map(int,input().split()))
    op.append(list2[0])
    l.append(list2[1]-1)
    r.append(list2[2]-1)
q = int(input())-1
for i in range(m):
    list3 = list1
    list1 = list1[0:l[i]]
    list4 = list3[l[i]:r[i]+1]
    list4.sort(reverse=(op[i]==1))
    list1.extend(list4)
    if r!=n-1:
        list1.extend(list3[r[i]+1:])
print(list1[q])