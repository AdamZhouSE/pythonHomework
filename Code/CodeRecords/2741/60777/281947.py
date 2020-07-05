temp=input()
temp=temp[1:len(temp)-1]
temp=[int(x) for x in temp.split(',')]
count=0
for i in range(len(temp)):
    most=1
    for j in range(i,len(temp)-1):
        if(temp[j+1]>temp[j]):
            most+=1
        else:
            break
    if(most>count):
        count=most
print(count)