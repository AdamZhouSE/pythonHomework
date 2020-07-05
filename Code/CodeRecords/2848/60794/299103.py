aa = input()
aaa = input().split(" ")
k = int(aaa[0])
m = int(aaa[1])
a = input().split(" ")
b = input().split(" ")
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(b)):
    b[i] = int(b[i])
list.sort(a)
list.sort(b)
bb = b[len(b)-m]
aa = a[k-1]
if aa >= bb:
    print("NO")
else:
    print("YES")