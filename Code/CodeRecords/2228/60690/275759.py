target=int(input())
n=0
list=[0]
stop=False
while stop==False:
    l=[]
    n += 1
    for i in list:
        if i+n==target or i-n==target:
            stop=True
            break
        else:
            l.append(i+n)
            l.append(i-n)

    list.clear()
    list=l[:]

print(n)
