num=list(input())
for c in range(len(num)):
    if(num[c]=='6'):
        num[c]='9'
        break;
num=''.join(num)
print(num)