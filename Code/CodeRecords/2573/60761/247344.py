def nthTerm(n):
    if(n==1 or n==2):
        return 2
    elif(n%2==1):
        return nthTerm(n-2)**2
    else:
        return nthTerm(n-2)**3

n=int(input())
for i in range(n):
    print(nthTerm(int(input())))
    