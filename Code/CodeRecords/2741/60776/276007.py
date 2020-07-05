a=input()
a=a.replace("[","")
a=a.replace("]","")
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
max=1
count=1
for i in range(0,len(b)-1):
    if b[i+1]>b[i]:
        count=count+1
    else:
        count=1
    if count>max:
        max=count
print(max)