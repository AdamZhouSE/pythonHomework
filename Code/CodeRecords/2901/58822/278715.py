def bin(a):
    if(a==0):
        return 0
    k=1
    sum=a%2
    while((a/2)!=0):
        a=int(a/2)
        k=k*10
        sum=k*(a%2)+sum
    return sum
if __name__=='__main__':
    n=int(input())
    res=str(bin(n))
    if(len(res)==1):
        print("True")
        exit()
    for i in range(len(res)-1):
        if res[i]==res[i+1]:
            print("False")
            exit()
    print("True")