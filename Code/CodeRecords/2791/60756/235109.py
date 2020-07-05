firstLine=input()
n=int(firstLine)
secondLine=input().split()
t=0
temp=1
ti=[]
for i in range(len(secondLine)):
    if int(secondLine[i])==1:
        t+=1
        if i!=0:
            ti.append(str(temp))
        temp=1
    else:
        temp+=1
ti.append(str(temp))
print(t)
print(' '.join(ti))