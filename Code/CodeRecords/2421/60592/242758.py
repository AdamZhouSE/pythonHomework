num = list(input())
for i in range(0,len(num)):
    if num[i]=='6':
        num[i]='9'
        break
print(''.join(num))