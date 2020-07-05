import re
time=int(input())
while(time>0):
    str11=input()
    result = ''.join(re.findall(r'[A-Za-z]',str11)) 
    result=result.lower()
    length=len(result)
    isH=True
    for i in range(length):
        if(result[i]!=result[length-i-1]):
            isH=False
    if(isH):
        print("YES")
    else:
        print("NO")
        

