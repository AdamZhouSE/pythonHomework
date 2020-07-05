n=int(input())
temp=n
i=1
count=0
while i<n:
    count+=1
    i*=2
num=2**(count-2)*3-1
list=[]
i=1
while i<count:
    if (n % 2 == 0):
        n=int(n/2)
        list.append(num-n)
        n=num-n
        if(num==5):
            i=count
        else:
            num=int((num-1)/2)

    else:
        n =int(n/2)
        list.append(num - n)
        n = num - n
        if (num == 5):
            i = count
        else:
            num =int((num - 1) / 2)
    i+=1
if(temp>3):
    list.append(1)
lenth=len(list)
j=1
newlist=[]
while j<=lenth:
    newlist.append(list[lenth-j])
    j+=1
newlist.append(temp)
print(newlist)