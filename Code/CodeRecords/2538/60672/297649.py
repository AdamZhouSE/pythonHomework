def strd(string):
    string=sorted(string)
    string2=sorted(string)
    for i in range(len(string)):
        if int(string[i])<=0:
            string2.remove(string[i])
    m=1
    if len(string2)==0:
        return m
    else:
        for i in range(len(string2)):
            if int(string2[i])==m:
                m=m+1
                continue
            elif int(string2[i])==m-1:
                m=m-1
                continue
            else:
                break
        return m
        

string=input()
k=strd(string)
print(k)