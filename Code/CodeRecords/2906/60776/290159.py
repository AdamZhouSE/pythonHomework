n=int(input())
zongzifu=input()
result=""
for i in range(0,len(zongzifu)):
    temp=chr((ord(zongzifu[i])-ord('a')+n)%26+97)
    result=result+temp
print(result,end="")