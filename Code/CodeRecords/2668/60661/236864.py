t=int(input())
for j in range(t):
    num=int(input())
    b=list(bin(num)[2:])
    res=2**(len(b)-1)*2-1
    print(str(res-num)+' '+str(res))