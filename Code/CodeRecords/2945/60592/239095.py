str = input()
boy = 0
girl = 0
i = 0
while i < len(str):
    if i<len(str)-2 and str[i]=='b' and str[i+1]=='o' and str[i+2]=='y':
        boy+=1
        i+=3
    elif str[i]=='o' and str[i]=='y':
        boy+=1
        i+=2
    elif i<len(str)-1 and str[i] =='b' and str[i+1]!='o':
        boy+=1
        i+=1
    elif i<len(str)-1 and str[i] == 'b' and str[i+1]=='o':
        boy+=1
        i+=2
    elif i<len(str)-1 and str[i]=='o' and str[i+1]!='y':
        boy+=1
        i+=1
    elif str[i]=='y':
        boy+=1
        i+=1
    else:
        i+=1
print(boy)
i = 0
while i < len(str):
    if i<len(str)-3 and str[i]=='g' and str[i+1]=='i' and str[i+2]=='r' and str[i+3]=='l':
        girl+=1
        i+=4
    elif i<len(str)-2 and str[i]=='g' and str[i+1]=='i' and str[i+2]=='r':
        girl+=1
        i+=3
    elif i<len(str)-1 and str[i]=='g' and str[i+1]=='i':
        girl+=1
        i+=2
    elif str[i]=='g':
        girl+=1
        i+=1
    elif i<len(str)-2 and str[i]=='i' and str[i+1]=='r' and str[i+2]=='l':
        girl+=1
        i+=3
    elif i<len(str)-1 and str[i]=='i' and str[i+1]=='r':
        girl+=1
        i+=2
    elif str[i]=='i':
        girl +=1
        i+=1
    elif i<len(str)-1 and str[i]=='r' and str[i+1]=='l':
        girl+=1
        i+=2
    elif str[i]=='r':
        girl+=1
        i+=1
    elif str[i]=='l':
        girl+=1
        i+=1
    else:
        i+=1
print(girl,end='')