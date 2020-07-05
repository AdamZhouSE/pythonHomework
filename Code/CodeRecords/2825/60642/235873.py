a = int(input())
b = []
e = 0

for i in range(a):
    c = input().split()
    d = int(c[0])+int(c[1])+int(c[2])+int(c[3])
    if(i==0):
        e = d
    b.append(d)

b.sort(reverse=True)
print(b.index(e)+1)