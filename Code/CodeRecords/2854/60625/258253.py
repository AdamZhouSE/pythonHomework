strList=input().split()
array=[]
for c in strList:
    array.append(int(c))
array.sort()
elementOfarray=list(set(array))

counts=[]
for index in range(len(elementOfarray)):
    counts.append(0)
    for num in array:
        if elementOfarray[index]==num:
            counts[index]+=1

if 6 in counts:
    print('Elephant')
elif 5 in counts:
    if counts[0]==1:
        print('Bear')
    else:
        print('Alien')
elif 4 in counts:    
        if 2 in counts:
            print('Elephant')
        else:
            if counts[0] == 4:
                print('Alien')
            else:
                print('Bear')
else:
    print('Alien')