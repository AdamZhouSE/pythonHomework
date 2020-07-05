n=int(input())
s=set(map(int,input().split(" ")))

step=0
if 0 in s:
    s.remove(0)
print(len(s))    