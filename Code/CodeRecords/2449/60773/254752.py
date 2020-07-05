s=input()
l=s.split(",")
n=input()
if n in l:
    print(l.index(n))
else:
    print(-1)