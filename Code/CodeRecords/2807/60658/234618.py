m,n=[int(x) for x in input().split()]
boxes = [int(x) for x in input().split()]
keys = [int(x) for x in input().split()]
odd = 0
even = 0
for i in boxes:
    odd+=1 if i%2==1 else 0
for i in keys:
    even+=1 if i%2==0 else 0
print(min(odd,even)+min(m-odd,n-even))