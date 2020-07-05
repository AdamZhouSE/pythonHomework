temp=input()
temp=temp[1:len(temp)-1]
temp=[int(x) for x in temp.split(',')]
h=max(temp)
right=False

while(not right):
    c=0
    for i in range(len(temp)):
        if(temp[i]>=h):
            c+=1
    if(c>=h):
        print(h)
        right=True
    h-=1
