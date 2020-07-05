def Test():
    n=int(input())
    nums=eval("["+input().strip().replace(" ",",")+"]")
    result=0
    for i in range(0,n):
        for j in range(i+1,n):
            result=max(result,nums[j]-nums[i])
if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()