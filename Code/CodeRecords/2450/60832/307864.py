ar = list(map(int, input().split(',')))
n=int(input())

x=-1
y=-1

open=False
for i in range(len(ar)):
    if ar[i]==n and not open:
        x=i
        open=True
    elif open and ar[i]!=n:
        y=i-1
        break
        

print([x,y])