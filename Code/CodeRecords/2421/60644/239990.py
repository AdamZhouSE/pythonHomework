num=input()
for i in range(0,len(num)):
    if num[i:i+1]=='6':
        num=num[0:i]+'9'+num[i+1:]
        break
print(num)
