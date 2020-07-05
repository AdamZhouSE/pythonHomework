NUM=int(input())
lst=list(map(int,input().split()))
i=0
j=len(lst)-1
firstPer=0
secPer=0
while i<=j:
    if lst[i]<lst[j]:
        firstPer+=lst[j]
        j-=1

        if i<=j:
            if lst[i]<lst[j]:
                secPer+=lst[j]
                j-=1
            else:
                secPer+=lst[i]
                i+=1
        else :
            break

    else :
        firstPer+=lst[i]
        i+=1
        if i<=j:
            if lst[i]<lst[j]:
                secPer+=lst[j]
                j-=1
            else:
                secPer+=lst[i]
                i+=1
        else :
            break
print(str(firstPer)+" "+str(secPer))


