null = 0
ls = eval(input())
for i in range(0,len(ls)):
    if ls[i]==None:
        continue
    else:
        if i*2+1<len(ls) and ls[i*2+1]!=None and ls[i*2+1]>ls[i]:
            print("false")
            break
        if i*2+2<len(ls) and ls[i*2+2]!=None and ls[i*2+2]<ls[i]:
            print("false")
            break
    if i == len(ls)-1:
        print("true")