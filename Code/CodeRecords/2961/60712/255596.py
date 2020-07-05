l = list(input())
l2 = []

for i in range(len(l)):
    s=""
    for j in range(i,i+len(l)):
        s=s+l[j%len(l)]
    l2.append(s)

l2.sort()
s=''
for i in range(len(l2)):
    s=s+l2[i][len(l)-1:len(l)]

print(s,end="")