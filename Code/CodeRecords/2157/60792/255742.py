str1=input()
len=len(str1)
sum=0
i=0
while i<len:
    if str1[i]=="I":
        if i+1<len and str1[i+1]=="V":
            sum=sum+4
            i=i+1
        elif i+1<len and str1[i+1]=="X":
            sum=sum+9
            i=i+1
        else:
            sum=sum+1
    elif str1[i]=="V":
        sum=sum+5
    elif str1[i]=="X":
        if i+1<len and str1[i+1]=="L":
            sum=sum+40
            i=i+1
        elif i+1<len and str1[i+1]=="C":
            sum=sum+90
            i=i+1
        else:
            sum=sum+10
    elif str1[i]=="L":
        sum=sum+50
    elif str1[i]=="C":
        if i+1<len and str1[i+1]=="D":
            sum=sum+400
            i=i+1
        elif i+1<len and str1[i+1]=="M":
            sum=sum+900
            i=i+1
        else:
            sum=sum+100
    elif str1[i]=="D":
        sum=sum+500
    elif str1[i]=="M":
        sum=sum+1000
    i=i+1
print(sum)