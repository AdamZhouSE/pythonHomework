n=input()
if int(n)>=0:
    result=''
    for i in range(len(n)):
        result+=n[len(n)-i-1]
    while result[0]=='0':
        result=result[1:len(result)]
else:
    result='-'
    for i in range(len(n)-1):
        result+=n[len(n)-i-1]
print(result)