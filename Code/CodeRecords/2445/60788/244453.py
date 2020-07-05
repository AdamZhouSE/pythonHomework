from sys import stdin
def feature(str):
    li=list(set(list(str)))
    li.sort()
    return [str.count(x) for x in li]

m=stdin.readline()
s=m.split(',')[0][3:]
a=s[1:len(s)-1]
t=m.split(',')[1][3:]
b=t[1:len(t)-1]
print((feature(a)==feature(b)).lower())
    