a=input()
a=a.replace("[","")
a=a.replace("]","")
b=a.split(',')
e=len(b)
result=[]
while(len(b)!=0):
    c=len(b)
    d=b[0]
    while d in b:
        b.remove(d)
    if c-len(b)> e/3:
        result.append(d)
for i in range(0,len(result)):
    result[i]=int(result[i])
print(result)