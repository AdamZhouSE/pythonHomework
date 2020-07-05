count=0
component=[int(x) for x in input().split(',')]
maximum=[int(x) for x in list(input())]
for i in range(1,len(maximum)):
    count+=pow(len(component),i)
for i in component:
    if i<maximum[0]:
        count+=pow(len(component),len(maximum)-1)
i=0
while maximum[i] in component:
    for j in component:
        if j<maximum[i+1]:
            count+=pow(len(component),len(maximum)-2-i)
    i+=1
    if i==len(maximum)-1:
        if maximum[i] in component:
            count+=1
        break
print(count)