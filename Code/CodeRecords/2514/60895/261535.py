s=input()
t=input()
length=len(t)
result=True
for item in s:
    for j in range(0,len(t)):
        if t[j]==item:
            t=t[(j+1):]
            break
    if len(t)==length:
        result=False
        break
    else:
        length=len(t)
print(result)