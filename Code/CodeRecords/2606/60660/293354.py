l=eval(input())
n=int(input())
try:
    print(l.index(n))
except ValueError:
    print(-1)