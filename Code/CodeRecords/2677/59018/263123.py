def Xors(N,a):
    dict={}
    for j in a:
        if j not in dict.keys():
            dict[j]=1
        else:
            dict[j]=dict[j]+1
            
    sum=0        
    for k in dict:
        if dict[k]>1:
            sum=sum+dict[k]*(dict[k]-1)/2
    return int(sum )  



T=int(input())
for i in range(T):
    N=int(input())
    info=input().split(' ')
    a=[int(y) for y in info]
    
    print(Xors(N,a))