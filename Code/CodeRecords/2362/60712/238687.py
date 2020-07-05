n = int(input())
temp = 0
result = 0
j=0
for i in range(n,0,-1):
    if j%4==0:
        if i>0:
            temp = i
            i=i-1
            if i>0:
                temp = temp*(i)
                i =i-1
                if i>0:
                    temp =int(temp/i)
        if j!=0:
            result =result -temp
        else:
            result=result+temp
    elif j%4==3:
        result =result+i
    j=j+1
print(result)