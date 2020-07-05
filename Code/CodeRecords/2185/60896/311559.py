import math
a=eval(input())
for i in range(a):
    n=eval(input())+1
    level=int(math.log(n,2))
    index=n-pow(2,level)
    s=bin(index)
    s=s[2:]
    for j in range(level-len(s)):
        s='0'+s
    result=''
    for i in range(level):
        if(s[i]=='0'):
            result+='4'
        else:
            result+='7'   
    print(result)