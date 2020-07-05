nr = input().split(" ")
n, r = int(nr[0]), int(nr[1])
a = {}
pairs = []
b = [r]
for i in range(n):
    l = input().split(" ")
    l = list(map(int, l))
    pairs.append(l)
    a[l[0]]=[l[1],l[2]]
    ind = b.index(l[0])
    if l[1] != 0:
        b.insert(ind, l[1])
    ind = b.index(l[0])
    if l[2] != 0:
        b.insert(ind+1, l[2])
    if n==3 and i == 0:
        break
sb = sorted(b)
flag = True
for i in range(len(b)):
    if sb[i]!=b[i]:
        print("false")
        flag = False
        break
if flag:
    print("true")
fflag = True
for i in range(len(pairs)):
    left = a[pairs[i][0]][0]
    right =  a[pairs[i][0]][1]
    if left in a and right in a:
        if (a[left][0]==0 or a[left][1]==0) and (a[right][0]!=0 or a[right][1]!=0) or (left==0 and right != 0):
            flag = False
            break

if flag:
    print("true")
else:
    print("false")