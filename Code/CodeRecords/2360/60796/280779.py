import math
def build(s,before,N,result):
    if len(before)==N:
        result.append(before)
        return
    i=0
    while i<len(s):
        if len(before)==0:
            build(s[:i]+s[i+1:],before+[s[i]],N,result)
        else:
            x=s[i]
            y=before[len(before)-1]
            if math.sqrt(x+y)%1==0:
                build(s[:i] + s[i + 1:],before+[x], N, result)
        i=i+1

ls=[]
str=input()
ls=str.split(",")
for i in range(len(ls)):
    ls[i]=int(ls[i])
result=[]
build(ls,[],len(ls),result)
i=0
while i<len(result):
    if result.count(result[i])>1:
        del result[i]
    else:
        i=i+1
print(len(result))
