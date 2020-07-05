count=int(input())
list=[]

while count>0:  #count sub
    sum=0
    r=int(input())
    length=0

    while length<r:
        width = 0.5
        length=length+0.5
        while width<r:
            if width**2+length**2<=r**2:
                sum=sum+1
            width=width+0.5

    list.append(sum)
    count=count-1
for i in list:
    print(i)