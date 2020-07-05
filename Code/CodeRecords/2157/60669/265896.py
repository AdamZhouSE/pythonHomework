string=input()
sum=0
arr=[]
special=["CD","CM","XL","XC","IV","IX"]
value=[400,900,40,90,4,9]
temp=""
i=0
while i<len(string)-1:
    front=string[i]
    behind=string[i+1]
    if front==behind:
        temp+=front
        if i==len(string)-2:
            arr.append(temp+behind)
        i+=1
    elif front+behind in special:
        arr.append(front+behind)
        i+=2
    else:   # 不同两个 还不是特殊的那个
        temp+=front
        arr.append(temp)
        temp=""
        i+=1

for item in arr:
    if item in special:
        index=special.index(item)
        sum+=value[index]
    else:
        for k in range(0,len(item)):
            if item[k]=="I":
                sum+=1
            elif item[k]=="V":
                sum+=5
            elif item[k]=="X":
                sum+=10
            elif item[k]=="L":
                sum+=50
            elif item[k]=="C":
                sum+=100
            elif item[k]=="D":
                sum+=500
            else:
                sum+=1000
print(sum)