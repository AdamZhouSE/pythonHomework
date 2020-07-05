numbers=list(map(int,input()[1:-1].split(",")))
odd=[]
even=[]
for i in numbers:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
for j in odd:
    even.append(j)
print(even)