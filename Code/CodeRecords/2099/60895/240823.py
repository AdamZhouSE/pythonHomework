s=input()
length=len(s)
temp=s[::-1]
index=1
result=0
for item in temp:
    num=ord(item)-ord('A')+1
    result=result+index*num
    index=index*26
print(result)