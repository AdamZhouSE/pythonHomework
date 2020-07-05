l=list(input())
width=len(l)
while width>1:
    index=0
    while index+width<=len(l):
        if len(list(set(l[index:index+width])))==width:
            print(width)
            index=-1
            break
        index+=1
    if index==-1:
        break
    width-=1
else:
    print(width)