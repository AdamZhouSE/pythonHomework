num=list(input())
print(num)
for c in num:
    print(c)
    if(c==54):
        c=57
        break;
num=''.join(num)
print(num)