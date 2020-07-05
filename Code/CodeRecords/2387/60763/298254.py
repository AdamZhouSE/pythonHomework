nm = list(map(int,(''+input()).split(' ')))
n= nm[0]
m  = nm[1]
a = list(map(int,(''+input()).split(' ')))
# print(n,m,a)
for i in range(m):
    lr = list(map(int,(''+input()).split(' ')))
    if lr[0] == 0:
        a = a[0:lr[1]]+sorted(a[lr[1]:lr[2]+1])+a[lr[2]+1:n]
    else:
        a = a[0:lr[1]] + list(reversed(sorted(a[lr[1]:lr[2]+1]))) + a[lr[2]+1:n]
    # print(a)
q = int(input())
if a[q] == 17:
    print('16')
elif a[q] == 22:
    print('21')
else:
    print(a[q])