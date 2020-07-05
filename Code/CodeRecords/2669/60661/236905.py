t=int(input())
for j in range(t):
    num=int(input())
    b=list(bin(num)[2:])
    end=2**(len(b)-1)*2-1
    store=[]
    for i in range(end+1):
        j=end-i
        if num&j==j:
            store.append(str(j))
    print(' '.join(store)+' ')
