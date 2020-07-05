n=list(eval(input()))
li=[]
for i in range(0,len(n)):
    k=n[i][1]
    if(k in li):
        print(n[i])
        break
    else:
        li.append(k)