a=input()
a=a.replace("[","")
a=a.replace("]","")
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
b.sort()
for i in range(len(b)-1,-1,-1):
    if b[i-1]<len(b)-i and b[i]>=len(b)-i:
        print(b[i])
        break