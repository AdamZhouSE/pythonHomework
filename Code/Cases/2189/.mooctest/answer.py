liste=[]
count=0
flag=-1
def happynum(n):
    global count
    sume=0
    num=n
    count+=1
    while(num>0):
        rem=num%10
        sume=sume+pow(rem,2)
        num=num//10
    if(sume==1):
        return 1
    elif((sume!=1 and sume in seen)):
        return 0
    seen.append(sume)
    return happynum(sume)
def recur(n):
    global boo
    for i in range(1000):
        n+=1
        count=0
        seen=[]
        seen.append(n)
        boo=happynum(n)
        if(boo==1):
            print(n)
            break
t=int(input())
for i in range(t):
    no=int(input())
    liste.append(no)
for i in range(t):
    seen=[]
    boo=0
    recur(liste[i])