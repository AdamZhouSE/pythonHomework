str=input()
dic=eval(input())
result=[]
for i in range(0,len(dic)):
    if dic[i] in str:
        result.append(dic[i])
if len(result)==0:
    print("")
else:
    index=0
    for i in range(1,len(result)):
        if len(result[index])<len(result[i]):
            index=i
    print(result[index])