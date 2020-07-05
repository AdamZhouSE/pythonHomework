arr=eval(input())
odd=[]
even=[]
for item in arr:
    if item%2==0:
        even.append(item)
    else:
        odd.append(item)
print(even+odd)