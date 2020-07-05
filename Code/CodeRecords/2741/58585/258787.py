source=input()
result=0
temp=0
if(source[1]>source[0]):
    result=2
    temp=2
for i in range(len(source)-2):
    i+=1
    if source[i+1]>source[i] or source[i+1]==source[i]:
        temp+=1
    else:
        temp=0
    if(temp>result):
        result=temp
print(result)