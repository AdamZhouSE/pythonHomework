num=input()
i=0
while i<len(num) and num[i]!='6':
    i=i+1
if i<len(num):
    result=num[:i]+'9'+num[i+1:]
else:
    result=num
print(result)