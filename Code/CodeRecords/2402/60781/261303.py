import re
n=int(input())
data2D = []
i=0
while i<n :
    i+=1
    userInput = input()
    info = re.split(r'[\D]',userInput)
    data = []
    try:
        for number in info:
            data+=[int(number)]
        data2D+=[data]
    except:
        break;
k=int(input())
j=1
lis=[]
res=0
while j<=k:
    i=0
    while i<n:
        if(data2D[i][0]<=j and data2D[i][1]>=j):
            res+=data2D[i][2]
        i+=1
    lis.append(res)
    res=0
    j+=1
print(lis)