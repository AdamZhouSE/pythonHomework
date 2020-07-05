str=input()
dic=eval(input())
result=[]
for i in range(0,len(dic)):
    mark=0
    for j in range(0,len(dic[i])):
       if dic[i][j] in str:
           continue
       else:
           mark=1
           break
    if mark==0:
       result.append(dic[i])
if len(result)==0:
    print("")
else:
    index=0
    for i in range(1,len(result)):
        if len(result[index])<len(result[i]):
            index=i
    print(result[index])