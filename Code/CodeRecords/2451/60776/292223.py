a=input()
a=a.replace("[","")
a=a.replace("]","")
a=a.replace(" ","")
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
target=b[len(b)-1]
b.sort()
for i in range(0,len(b)):
    if b[i]==target:
        print(i)
        break