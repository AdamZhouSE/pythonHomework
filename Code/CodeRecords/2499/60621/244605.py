a=input()
a=int(a)
question=[]
delBase=0
for i in range(a):
    temp=input().split()
    if(temp[0]=="Add"):
        delBase+=1
        te=[int(x) for x in temp[1:]]+[delBase]
        question.append(te)
    elif temp[0]=="Query":
        x=int(temp[1])
        count=0
        for j in question:
            if(j[0]*x+j[1]>j[2]):
                count+=1
        print(count)
    elif temp[0]=="Del":
        num=0
        for k in question:
            if(k[3]==int(temp[1])):
                num=k
                break
        question.remove(num)
