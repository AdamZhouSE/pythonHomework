def isdengcha(list):
    chazhi=list[1]-list[0]
    for i in range(1,len(list)-1):
        if list[i+1]-list[i]!=chazhi:
            return False
    return True



b=input().split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
result=0
for i in range(0,len(b)-2):
    for j in range(i+2,len(b)):
        if isdengcha(b[i:j+1]):
            result=result+1
        else:
            break
print(result)