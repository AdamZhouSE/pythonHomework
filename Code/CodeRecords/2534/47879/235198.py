a=input()
a=a[2:len(a)-2]
a=a.replace("][","],[")
b=a.split('],[')
list1=[]
for i in range(len(b)):
    c=b[i][0:len(b[i])]
    c=c.replace(" ","")
    d=c.split(',')
    for j in range(len(d)):
        list1.append(int(d[j]))
list1.sort()
print(list1)