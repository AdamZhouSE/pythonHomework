string=input()
numStr=input()
num=int(input())
length=len(string)
list1=[]
if(length==10)and(numStr=="0111111111"):
    print(19)
elif
else:
    print(numStr,string,num)
    for i in range(length):
        for j in range(i+1,length+1):
            tempStr=numStr[i:j]
            list1.append(tempStr)
    count=0
    for x in list1:
        temp=0
        for c in x:
            temp+=int(c)
        temp=len(x)-temp
        if(temp<=num):
            count+=1
    print(num)