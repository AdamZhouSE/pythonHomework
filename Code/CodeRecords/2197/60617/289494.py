def killing_ring():
    men=int(input())
    left=men
    sword=0
    soldier=[1]*men
    while left!=1:
        kill=(sword+1)%men
        while soldier[kill]!=1:
            kill += 1
            kill = kill %men
        soldier[kill]=0
        left-=1
        sword=(kill+1)%men
        while soldier[sword]!=1:
            sword+=1
            sword=sword%men
    for i in range(0,men):
        if soldier[i]==1:
            print(i+1)

if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        killing_ring()
