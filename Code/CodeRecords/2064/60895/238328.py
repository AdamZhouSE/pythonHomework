s=input()
num=0        
for i in range(0,len(s)-1):
    a=s[i]
    b=s[i+1]
    temp=a+b
    if temp=='IV' or temp=='IX' or temp=='XL' or temp=='XC' or temp=='CD' or temp=='CM':
        if a=='I':
            num=num-1
        elif a=='X':
            num=num-10   
        elif a=='C':
            num=num-1000
        else:
            num=num+0
        if b=='V':
            num=num+5
        elif b=='X':
            num=num+10
        elif b=='L':
            num=num+50   
        elif b=='C':
            num=num+100
        elif b=='D':
            num=num+500
        elif b=='M':
            num=num+1000
        else:
            num=num+0
        i=i+1
    else:
        if a=='I':
            num=num+1
        elif a=='V':
            num=num+5
        elif a=='X':
            num=num+10
        elif a=='L':
            num=num+50   
        elif a=='C':
            num=num+100
        elif a=='D':
            num=num+500
        else:
            num=num+1000
if s[len(s)-1]=='I':
    num=num+1
elif s[len(s)-1]=='V':
    num=num+5
elif s[len(s)-1]=='X':
    num=num+10
elif s[len(s)-1]=='L':
    num=num+50   
elif s[len(s)-1]=='C':
    num=num+100
elif s[len(s)-1]=='D':
    num=num+500
else:
    num=num+1000            
print(num)