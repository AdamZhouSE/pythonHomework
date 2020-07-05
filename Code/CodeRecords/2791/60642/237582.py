input()
n = 0
m = ""
b = []
c = 0
a = input().split()
for i in range(len(a)):
    b.append(int(a[i]))

for i in range(len(b)):
    if( b[i]<=c ):
        m = m + str(c) + " "
        n = n+1
    c = b[i]
    if( i==len(b)-1 ):
        m = m + str(c) + " "
        n = n + 1

print(n)
print(m[0:-1])