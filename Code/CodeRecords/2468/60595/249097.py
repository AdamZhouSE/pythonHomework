def Test():
    n=int(input())
    nums=eval("["+input().strip().replace(" ",",")+"]")
    P=[]
    for i in range(0,n):
        P.append(get(i,nums))
    print(P)
def get(i,nums):
    c=1
    for j in range(0,len(nums)):
        if(i!=j):
            c=c*nums[j]
    return c

if __name__ == "__main__":
    total = int(input())
    for i in range(0, total):
        Test()