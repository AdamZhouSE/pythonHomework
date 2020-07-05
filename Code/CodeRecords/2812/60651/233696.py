people=int(input())
inlist=input().split()
inset=set(inlist)
inset.discard("0")
print(len(inset))

