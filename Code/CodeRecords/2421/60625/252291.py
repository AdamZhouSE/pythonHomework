num=input()
for index in range(len(num)):
    if num[index]=='6':
        num=num[:index]+'9'+num[index+1:]
        break
print(num)