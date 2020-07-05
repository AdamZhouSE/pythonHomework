dic={
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000,
}
s=input()
n=len(s)
result=""
for i in range(n):
    num=int(s[i])
    if n-i==4:
        result=result+'M'*num
    elif n-i==3:
        if num==9:
            result=result+'CM'
        elif num<4:
            result=result+'C'*num
        elif num==4:
            result=result+'CD'
        elif num==5:
            result=result+'D'
        else:
            result=result+'D'+'C'*(num-5)
    elif n-i==2:
        if num==9:
            result=result+'XC'
        elif num<4:
            result=result+'X'*num
        elif num==4:
            result=result+'XL'
        elif num==5:
            result=result+'L'
        else:
            result=result+'L'+'X'*(num-5)
    else:
        if num==9:
            result=result+'IX'
        elif num<4:
            result=result+'I'*num
        elif num==4:
            result=result+'IV'
        elif num==5:
            result=result+'V'
        else:
            result=result+'V'+'I'*(num-5)
print(result)