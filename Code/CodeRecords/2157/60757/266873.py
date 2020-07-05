str=input()
count=0
for i in range(len(str)):
    if str[i]=='V':
        count=count+5
    elif str[i]=='L':
        count=count+50
    elif str[i]=='D':
        count=count+500
    elif str[i]=='M':
        count=count+1000
    elif str[i]=='I':
        if i<len(str)-1 and (str[i+1]=='V' or str[i+1]=='X'):
            count=count-1
        else:
            count=count+1
    elif str[i]=='X':
        if i<len(str)-1 and (str[i+1]=='L' or str[i+1]=='C'):
            count=count-10
        else:
            count=count+10
    elif str[i]=='C':
        if i<len(str)-1 and (str[i+1]=='D' or str[i+1]=='M'):
            count=count-100
        else:
            count=count+100
print(count)
            