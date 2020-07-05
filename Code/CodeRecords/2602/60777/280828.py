temp=input()
temp=temp[1:len(temp)-1]
a=temp.split(',')
temp=input()
temp=temp[1:len(temp)-1]
b=temp.split(',')

l=min(len(a),len(b))
find=False
while(True):
    res1=[]
    res2=[]
    for i in range(0,len(a)-l+1):
        res1.append(a[i:i+l])
    for i in range(0,len(b)-l+1):
        res2.append(b[i:i+l])
    for x in res1:
        if x in res2:
            find=True
            break
    if(find):
        break
    l-=1
print(l)