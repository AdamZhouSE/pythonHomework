def Func(a,b):
    result=0
    Len=len(a)
    if len(a)>len(b):
        Len=len(b)
    for leng in range(Len):
        for aStart in range(len(a)-Len+leng+1):
            for bStart in range(len(b)-Len+leng+1):
                iS=1
                for i in range(Len-leng):
                    if a[aStart+i]!=b[bStart+i]:
                        iS=0
                        break
                if iS==1:
                    return Len-leng
    return result

string=input()
string=string.replace('[','')
string=string.replace(']','')
List1=list(map(int,string.split(',')))
string=input()
string=string.replace('[','')
string=string.replace(']','')
List2=list(map(int,string.split(',')))
print(Func(List1,List2))