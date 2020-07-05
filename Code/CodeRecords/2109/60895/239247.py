s=input()
result=s
length=len(result)
while length>1:
    num=0
    for item in result:
        num=num+int(item)
    result=str(num)
    length=len(result)
print(result)