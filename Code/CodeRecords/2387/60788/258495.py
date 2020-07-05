from sys import stdin
line1=stdin.readline()
num=int(line1.split()[1])
s=[int(x) for x in stdin.readline().split()]
for i in range(num):
    line=stdin.readline()
    t=[int(x) for x in line.split()]
    start=t[1]
    end=t[2]
    c=s[start:end]
    c.sort(reverse=(t[0]==1))
    s=s[0:start]+c+s[end:]
print(s[int(input().strip())-1])