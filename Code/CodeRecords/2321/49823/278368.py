def az(l,n):
    # TODO
    n=str(n)
    nn=len(n)
    r=sum(len(l)**i for i in range(1,nn))
    i=0
    while i<nn:
        r+=sum(c<n[i] for c in l)*(len(l)**(nn-i-1))
        if n[i] not in l:
            break
        i+=1
    print(r+(i==n))
if __name__ == '__main__':
    az([int(i) for i in input()],int(input()))
