S=input()
T=input()
str=''
for m in range(0,len(S)):
    repeat=0
    for n in range(0,len(T)):
        if T[n]==S[m]:
            repeat=repeat+1
    for i in range(0,repeat):
        str=str+S[m]
    if(repeat>0):
        T=T.replace(S[m],'')
print(str+T)