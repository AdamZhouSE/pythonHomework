t=int(input())
for i in range(0,t):
    name=list(input())
    less=list(set(name))
    num=[]
    for j in range(0,len(less)):
        if less[i]!='a' and less[i]!='e' and less[i]!='i' and less[i]!='o' and less[i]!='u' :
            num.append(name.count(less[j]))
        
    if num.count(1)%2==0:
        print("SHE!")
    else:
        print("HE!")