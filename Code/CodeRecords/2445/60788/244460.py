from sys import stdin
def feature(str):
    li=list(set(list(str)))
    li.sort()
    return [str.count(x) for x in li]

m=stdin.readline()
s=m.split(',')[0][6:]
a=s[0:len(s)-1]
t=m.split(',')[1][6:]
b=t[0:len(t)-1]
print(str((feature(a)==feature(b))).lower())
    