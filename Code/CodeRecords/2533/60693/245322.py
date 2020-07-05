arr=eval(input())
odd,even=[],[]
for i in arr:
    if int(i)%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even+odd)