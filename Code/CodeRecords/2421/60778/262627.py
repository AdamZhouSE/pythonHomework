num=list(input())
for c in num:
    if(c=='6'):
        c='9'
        break;
num=''.join(num)
print(num)