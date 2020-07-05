input=input()
temp1=input.replace('[','')
temp2=temp1.replace(']','')
temp3=temp2.replace('\n','')
strfinall=temp3.split(',')
result=[];
for x in range(0,len(strfinall)):
    num=0
    for y in range(x+1,len(strfinall)):
        if strfinall[y]<strfinall[x]:
            num=num+1
    result.append(num)
print(result)