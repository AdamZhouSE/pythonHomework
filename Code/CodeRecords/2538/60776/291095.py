a=input()
a=a.replace("[","")
a=a.replace("]","")
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
b.sort()
for i in range(1,100000):
    if i not in b:
        print(i)
        break