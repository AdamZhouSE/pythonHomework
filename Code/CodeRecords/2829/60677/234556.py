n=int(input())
lie=input().split()
lie=[int(x) for x in lie]
li=list(set(lie))
li.sort()
if li[-2]-li[0]>li[-1]-li[1]:
    print(li[-1]-li[1])
else:
    print(li[-2]-li[0])