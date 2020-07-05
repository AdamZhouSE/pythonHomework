num=int(input())
# dict={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
arr=[1000,100,10,1]
record=[]
result=""
for i in range(0,len(arr)):
    temp=int(num/arr[i])
    record.append(temp)
    num-=(temp*arr[i])
for i in range(0,4):
    if i==0:
        for k in range(0,record[i]):
            result+="M"
    elif i==1:
        value = record[i]
        if value==4:
            result+="CD"
        elif value==9:
            result+="CM"
        else:
            if value >= 5:
                result+="D"
                value-=5
            for k in range(0,value):
                result+="C"
    elif i==2:
        value = record[i]
        if value == 4:
            result += "XL"
        elif value == 9:
            result += "XC"
        else:
            if value >= 5:
                result += "L"
                value -= 5
            for k in range(0, value):
                result += "X"
    elif i==3:
        value = record[i]
        if value == 4:
            result += "IV"
        elif value == 9:
            result += "IX"
        else:
            if value >= 5:
                result += "V"
                value -= 5
            for k in range(0, value):
                result += "I"
print(result)