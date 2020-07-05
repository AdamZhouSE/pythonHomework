a=input()
a=a.replace("[","")
a=a.replace("]","")
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
result=1
for i in range(0,len(b)-1):
    if b[i]<b[i+1]:
        result=result+1
print(result)