nk=input().split(' ')
n=int(nk[0]);k=int(nk[1])
mums=['']
for i in range(n):
    info=input().split(' ')
    name=info[0];mum=int(info[1])
    mums.append(name+mums[mum])
for j in range(k):
    start=input()
    count=0
    for k in range(len(mums)):
        if mums[k].startswith(start):
            count+=1
    print(count)