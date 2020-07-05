a=list(map(int,eval(input())))
even=[]
odd=[]
for i in a:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
even.extend(odd)
print(even)