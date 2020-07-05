nums=int(input())
inputStr=[" "]*nums
for i in range(0,nums):
    inputStr[i]=input()

cdn=inputStr
x_base=eval(cdn[1])[0]-eval(cdn[0])[0]
y_base=eval(cdn[1])[1]-eval(cdn[0])[1]
firstPoint=eval(cdn[0])
res=True
for i in range(1:nums):
    i=eval(cdn[i])
    if(x_base==0):
        if(i[0]-firstPoint[0]!=0):
            res=False
            break;
    elif(y_base==0):
        if(i[1]-firstPoint[1]!=0):
            res=False
            break;
    elif((i[0]-firstPoint[0])/(i[1]-firstPoint[1])!=x_base/y_base):
        res=False
        break;
print(res)