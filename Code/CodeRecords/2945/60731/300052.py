s=input()
num1=0
num2=0
i=0
while(i<=len(s)-1):
    if s[i:i+3]=='boy' and i<=len(s)-3:
        num1+=1
        i+=3
    elif s[i:i+4]=='girl' and i<=len(s)-4:
        num2+=1
        i+=4
    else:
        if s[i]=='b'or s[i]=='o'or s[i]=='y':
            num1+=1
        elif s[i]=='g'or s[i]=='i'or s[i]=='r' or s[i]=='l':
            num2+=1
        i+=1

print(num1)
print(num2,end='')