def Test():
    s=int(input())
    a=do(s-1)
    print(a)
def do(n):
    k=1
    nums=0
    for i in range(0,n):
        for j in range(0,k):
            nums=nums+1
        k=k+1
    result=1
    nums=nums+1
    for i in range(0,k):
        result=result*nums
        nums=nums+1
    return result

if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()