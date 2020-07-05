#02


n = int(input())
s = input()

for i in range(1,n):
    ss = input()
    x = s.find(ss[0])
    l = list(s)
    l.remove(l[x])
    l.insert(x,ss)
    s = "".join(l)

for i in range(0,len(s)):
    if s[i] != "*":
        print(s[i],end='')


