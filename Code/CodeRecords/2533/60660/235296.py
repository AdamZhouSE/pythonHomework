orgstr=input()[1:-1].split(',')
org=[int(orgstr[i]) for i in range(len(orgstr))]
odd=[]
even=[]
for num in range(len(org)):
    if not org[num]%2==0:
        odd.append(org[num])
    else:
        even.append(org[num])
print(even+odd)