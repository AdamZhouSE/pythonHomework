"""str=input()
newStr=str[::-1]
newStr=str+newStr
print(newStr)"""

def f(s):
    s=list(s)
    if len(s)<=1:
	    return s
    
    i=0
    length=len(s)/2
    while i<length:
        tmp=s[i]
        s[i]=s[len(s)-1-i]
        s[len(s)-1-i]=tmp
        i=i+1    
        strings=''.join(s)
        return strings
s=input()
print (s+f(s))