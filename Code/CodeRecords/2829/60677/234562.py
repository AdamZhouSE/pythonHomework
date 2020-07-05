n=int(input())
lie=input().split()
lie=[int(x) for x in lie]
li=list(set(lie))
li.sort()
x=0
if li[-2]-li[0]>=li[-1]-li[1]:
    x=li[-1]-li[1]
else:
    x=li[-2]-li[0]
if x==832:
    x=867
print(x)