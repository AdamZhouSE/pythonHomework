lists=eval(input())
even=[]
odd=[]

for i in lists:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

even.extend(odd)
print(even)