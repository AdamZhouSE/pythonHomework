n=input()
s=input()
l=len(s)
s=s.replace("VK","")
result=(l-len(s))//2
if("VV"in s or 'KK' in s):
    result=result+1
print(result,end="")