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
            j=j-1
        j=n-1
        i=i+1
    print(result)

if __name__ == "__main__":
    total=int(input())
    for i in range(total):
        Test()