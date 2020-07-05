data=list(input())
data_copy=data.copy()
tmp=[]
res=[]
pos=0
model=0
flag=False

while len(data_copy)!=0:
    newPop=data_copy[0]
    if len(data_copy)!=1:
        data_copy=data_copy[1:]
    else:
        data_copy.pop()
    if newPop=='(':
        tmp.append(newPop)
    elif len(tmp)==0:
        pos=len(data)-len(data_copy)
    elif newPop==")":
        tmp.pop()
if len(tmp)!=0:
    flag=True

i = pos-1
while i >=0:
    if data[i] == ')':
        j=len(data)-1
        if flag==True:
            while data[j]!='(':
                j-=1
            temp = data[0:i] + data[i + 1:j]+data[j+1:]
        else:
            temp=data[0:i]+data[i+1:]
        temp = "".join(temp)
        if temp not in res:
            res.append(temp)
    i -= 1

print(res)