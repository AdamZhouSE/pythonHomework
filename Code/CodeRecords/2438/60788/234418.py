from sys import stdin
s=stdin.readline()
t=s[1:len(s)-1]
m=t.split(',')
m.sort(reverse=False)
l=[int(x) for x in m ]
print(l)
