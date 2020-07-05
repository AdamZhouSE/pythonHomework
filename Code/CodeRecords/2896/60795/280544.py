newspaper=list(input())
letter=list(input())
mark=0
for i in range(0,len(letter)):
    if letter[i]==' ':
        continue
    else:
        tem=letter[i]
        if tem in newspaper:
            continue
        else:
            mark=1
            break
if mark==1:
    print("NO",end="")
else:
    print("YES",end="")
