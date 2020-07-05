k=input()
count=0
flag = 0
begin = 0
end=0
s=""
t=""
for i in range(len(k)):
    if(k[i]=='"' and flag == 0):
        begin = i
        flag = 1
        continue
    if(k[i]=='"' and flag==1):
        flag = 0
        end = i
        if(count==0):
            s=k[begin+1:end]
            count=count+1
        else:
            t=k[begin+1:end]
if(len(s)!=len(t)):
    print("false")
    exit()
l=list(s)
l.sort()
s="".join(l)
l=list(t)
l.sort()
t="".join(l)
if(s!=t):
    print("false")
    exit()
else:
    print("true")
    exit()
