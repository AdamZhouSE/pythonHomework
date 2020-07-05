def find_Primes():
    row=input().split(" ")
    left=int(row[0])
    right=int(row[1])
    res=[]
    for i in range(left+1,right):
        if(is_Prime(i)):
            res.append(i)
    for num in res:
        print(num, end=" ")
    print()
    
def is_Prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        find_Primes()