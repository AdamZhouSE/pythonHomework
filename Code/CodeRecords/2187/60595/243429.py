def Test():
    total=int(input())
    for i in range(0,total):
        s=input().split()
        n=int(s[0])
        k=int(s[1])
        nums=eval("["+input().strip().replace(" ",",")+"]")
        result=0
        for i in range(0,n):
            sum=0
            if(i+k<=n):
                for j in range(i,i+k):
                    sum=sum+nums[j]
            result=max(result,sum)
        print(result)


if __name__ == "__main__":
    Test()