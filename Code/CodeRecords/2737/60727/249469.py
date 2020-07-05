a=input()
li = a[1:len(a)-1].split(',')
li=sorted(li)
res=[]
if len(li)<=6:
    res.append(int(li[len(li)//3]))
else:
    res.append(int(li[len(li)//3]))
    res.append(int(li[len(li)//3*2]))
print(res)