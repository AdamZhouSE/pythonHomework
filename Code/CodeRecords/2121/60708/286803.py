def find(n):
    if n==1:
        return 10
    else:
        temp=9
        k=9
        for i in range(1,n):
            temp=temp*k
            k=k-1
        return find(n-1)+temp
if __name__ == '__main__':
    n=int(input())
    print(find(n))