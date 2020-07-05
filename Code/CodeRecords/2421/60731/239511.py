num=input()
list=list(num)
for i in range(len(list)):
    if list[i]=='6':
        list[i]='9'
        break
str=''.join(list)
print(int(str))