temp=input()
temp=temp[1:len(temp)-1]

temp=[int(x) for x in temp.split(',')]
even=[]
odd=[]

for x in temp:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
        
print(even+odd)