l=input()[1:-1]
l=l.split(',')
result=0
for i in range(len(l)):
    if l[i]>l[i+1]:
        result=i
        break
print(result)