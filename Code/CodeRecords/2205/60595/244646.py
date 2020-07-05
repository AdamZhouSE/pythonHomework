def Test():
    s=int(input())
    a=do(s//2)
    print(a)
def do(n):
    if(n==0 or n==1):
        return 1
    else:
        sum=0
        for i in range(0,n):
            sum=sum+do(i)*do(n-i-1)
        return sum
if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()