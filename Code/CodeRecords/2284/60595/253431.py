def Test():
    n=int(input())
    nums=eval("["+input().strip().replace(" ",",")+"]")
    i=0
    j=n-1
    result=0
    for m in range(0,n):
        while(i!=j):
            if(nums[j]-nums[i]>0):
                result=max(result,j-i)
            i=i+1
        i=0
    print(result)

if __name__ == "__main__":
    total=int(input())
    for i in range(total):
        Test()