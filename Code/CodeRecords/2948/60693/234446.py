names=list(input())
num=int(input())
numstr=''
for s in names:
    numstr=numstr+str(ord(s)-ord('A')+num)

while(numstr!='100' and len(numstr)>2):
    tmpstr=''
    for x in range(len(numstr)):
        if(x!=len(numstr)-1):
            tmpstr=tmpstr+str((int(numstr[x])+int(numstr[x+1]))%10)
            # print(newstr)
    numstr=tmpstr
   

print(int(numstr),end='')