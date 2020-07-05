ch=[[] for i in range(100)]
I=0
J=0
while(1):
    try:
        temp=str(input())
        if temp=='9':
            I+=1
            J=0
        if temp!='9':
            ch[I].append(temp)
        J+=1
    except:
        break

for k in range(I):
    jd=True
    for i in range(len(ch[k])):
        for j in range(i+1,len(ch[k])):
            if ch[k][i].find(ch[k][j])==0 or ch[k][j].find(ch[k][i])==0:
                jd=False
                break
    if jd:
        print("Set",k+1,"is immediately decodable")
    else:
        print("Set",k+1,"is not immediately decodable")
