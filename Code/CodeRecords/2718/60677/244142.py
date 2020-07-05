import re
string=list(input())
num=re.split('\D',input())
num2=[]
for i in range(num.__len__()):
    if i%4==2:
        num2.append([int(num[i]),int(num[i+1])])
num=[set(x) for x in num2]
for i in num:
    for j in num:
        if i.intersection(j) and i!=j:
            num.append(i.union(j))
            num.remove(i)
            num.remove(j)
if num[0].__len__()==string.__len__():
    string.sort()
    print("".join(string))

else:
    num=[list(x) for x in num]
    try:
        for i in num:
            if i[0]<i[1] and string[i[0]]>string[i[1]]:
                x=string[i[0]]
                string[i[0]]=string[i[1]]
                string[i[1]]=x
            if i[0]>i[1] and string[i[0]]<string[i[1]]:
                x=string[i[0]]
                string[i[0]]=string[i[1]]
                string[i[1]]=x
        print("".join(string))
    except:
        print(num)