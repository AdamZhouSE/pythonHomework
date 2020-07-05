t=int(input())
for i in range(0,t):
    name=list(input())
    less=list(set(name))
    num=[]
    for j in range(0,len(less)):
        num.append(name.count(less[j]))
    if num.count(1)%2==0:
        print("SHE! ")
    else:
        print("HE!")