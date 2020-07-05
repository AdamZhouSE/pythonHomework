a= input()
li = a[1:len(a)-1].split(',')
data=[]
for i in li:
    data.append(i[1:len(i)-1])
res=0
for i in data:
    for j in data:
        flag = 0
        if i!=j:
            for m in i:
                if m in j:
                    flag= 1
                    break
            if flag==0 and len(i)*len(j)>res:
                res=len(i)*len(j)
print(res)
            