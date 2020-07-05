a=eval(input())
for i in range(1,len(a)):
    head=0
    tail=i
    while head<tail:
        middle=(head+tail)//2
        if(a[middle]>a[i]):
            tail=middle

        else:
            head=middle+1
    temp=a[i]
    a.remove(temp)
    a.insert(head,temp)

print(a)