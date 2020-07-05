numOftests = int(input())
n = [i for i in range(200)]
a = [2*(n[i]+1)+1 for i in range(200)]
b = []
b.append(2)
for i in range(1,200):
    b.append(b[i-1]+a[i-1])
c = [b[i]*(n[i]+1) for i in range(200)]
list0 = []
for i in range(numOftests):
    list0.append(int(input()))
for x in list0:
    print(c[x-1])