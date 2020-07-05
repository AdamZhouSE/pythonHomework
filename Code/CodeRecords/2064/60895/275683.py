s=input()
num=0
for j in range(0,len(s)):
    a=s[j]
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
for i in range(0,len(s)-1):
    a=s[i]
    b=s[i+1]
    temp=a+b
    if temp=='IV' or temp=='IX' or temp=='XL' or temp=='XC' or temp=='CD' or temp=='CM':
        if a=='I':
            num=num-2
        elif a=='X':
            num=num-20   
        elif a=='C':
            num=num-200
        else:
            num=num+0         
print(num)