def Test():
    s=int(input())
    a=do(s)
    print(a)
def do(n):
    k=1
    nums=0
    result=0
    for i in range(0,n):
        m=1
        for j in range(0,k):
            nums=nums+1
            m=m*nums
        result=result+m
        k=k+1
    return result

if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()