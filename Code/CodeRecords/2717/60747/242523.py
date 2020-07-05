s=input()
equations=s[1:len(s)-1].split(",")
class DSU(object):
    def __init__(self):
        self.m = range(26)

    def f(self, x):
        if self.m[x] != x:
            self.m[x] = self.f(self.m[x])
        return self.m[x]

    def u(self, x, y):
        px = self.f(x)
        py = self.f(y)
        self.m[px] = py

dsu = DSU()
for eq in equations:
    if eq[1] == '=':
        dsu.u(ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a'))
a=0
for eq in equations:
    if eq[1] == '!':
        if dsu.f(ord(eq[0]) - ord('a')) == dsu.f(ord(eq[3]) - ord('a')):
            print("false") 
            a=-1
if a!=-1:
    print("true")



