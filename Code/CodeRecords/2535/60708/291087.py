num=eval(input())
i=0
result=0
check2=False
while(True):
    j=i+1
    while(True):
        check = True
        temp=num[i:j]
        for k in range(i,j):
            if not k in temp:
                check=False
                j=j+1
                break
        if(check):
            result=result+1
            i=j-1
        if(j==len(num)+1):
            check2=True
            break
    if(check2):
        break
print(result)