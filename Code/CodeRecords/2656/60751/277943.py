def change(num):
    result=""
    while(num!=0):
        result+=str(num%2)
        num=num//2
    return result
num=int(input())
for i in range(num):
    l=input().split(" ")
    M=int(l[0])
    N=int(l[1])
    M_=change(M)
    N_=change(N)
    while(len(M_)!=len(N_)):
        if M<N:
            M_+="0"
        elif M>N:
            N_+="0"
        else:
            pass
    a=-1
    for j in range(len(M_)):
        if M_[j]!=N_[j]:
            a=j
            break
    print(a+1)