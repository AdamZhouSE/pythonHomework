input()
x=set(map(int,input().split()))
if 0 in x: x.remove(0)
print(len(x))