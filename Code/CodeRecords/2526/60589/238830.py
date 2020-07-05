root1=input()[1:-1].split(',')
root2=input()[1:-1].split(',')
result=[]
for a in root1:
    if a!='null' and a!='':
        result.append(int(a))
for a in root2:
    if a!='null'and a!='':
        result.append(int(a))
result.sort()
print(result)