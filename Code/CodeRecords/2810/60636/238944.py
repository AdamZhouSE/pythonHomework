number=int(input())
binary=[]
for i in range(1,number):
    if(list(str(i)).count("0")+list(str(i)).count("1")==len(list(str(i)))):
        binary.append(i)
result=[]
while(number!=0):
    for a in range(len(binary)):
        if(a==len(binary)-1):
            number=number-binary[a]
            result.append(binary[a])
            break
        elif(binary[a+1]>number):
            number=number-binary[a]
            result.append(binary[a])
            break
ans=""
for i in result:
    ans=ans+str(i)+" "
print(len(result))
print(ans[:-1])