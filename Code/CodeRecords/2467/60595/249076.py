def Test():
    m,n,k=map(int,input().split())
    A=eval("["+input().strip().replace(" ",",")+"]")
    B=eval("["+input().strip().replace(" ",",")+"]")
    A.extend(B)
    A.sort()
    print(A[k-1])
if __name__ == "__main__":
    total = int(input())
    for i in range(0, total):
        Test()