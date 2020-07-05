temp=input()
temp=temp[1:len(temp)-1]

li=[int(x) for x in temp.split(',')]
start=-1
end=-1
for i in range(len(li)-1):
    if(li[i+1]<li[i]):
        if(start==-1):
            start=i
            end=i+1
        else:
            end=i+1            
print(end-start+1)