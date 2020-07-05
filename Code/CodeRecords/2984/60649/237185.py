string1=input()
string2=input()
if(len(string2)==0):
    string2=input()
if(string1[len(string1)-1]==' '):
    string1=(string1[0:len(string1)-1])
if len(string1)!=len(string2):
    print(1)
else:
    is3=True
    for i in range(0,len(string1)):
        k=ord(string2[i])-ord(string1[i])
        if k==0:
            continue
        else:
            is3=False
            if(k!=-32) and(k!=32):
                print(4)
                break
    else:
        if is3:
            print(2)
        else:
            print(3)
