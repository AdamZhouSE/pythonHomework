str=input()
list=[]
for i in range(len(str)):
    if str[i]!=']':
        list.append(str[i])
    else:
        temp=[]
        while list[-1]!='[':
            temp.append(list[-1])
            list.pop()
        list.pop()
        temp1=[]
        for j in range(len(temp)):
            temp1.append(temp[len(temp)-j-1])
        num=int(temp1[0])
        if num==1:
            num=10+int(temp1[1])
            temp1.pop(0)
        temp1.pop(0)
        res=[]
        for j in range(num):
            for k in range(len(temp1)):
                res.append(temp1[k])
        for j in res:
            list.append(j)
string=''.join(list)
print(string,end='')