t=int(input())
for i in range(0,t):
    name=list(input())
    less=list(set(name))
    num=[]
    re=''
    
    for j in range(0,len(less)):
        if less[i]!='a' and less[i]!='e' and less[i]!='i' 
        and less[i]!='o' and less[i]!='u' and less[i] not in re:
        re+=less[i]
    if len(re)%2==0:
        print("SHE!")
    else:
        print("HE!")