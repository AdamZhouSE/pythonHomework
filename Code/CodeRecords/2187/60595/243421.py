def Test():
    total=int(input())
    for i in range(0,total):
        s=input().split()
        n=int(s[0])
        k=int(s[1])
        nums=eval("["+input()+"]")
        result=0
        for i in range(0,n):
            if(i+k<n):
                sum=0
                for j in range(i,i+k):
                    sum=sum+nums[j]
                    result=max(result,sum)
        print(result)


if __name__ == "__main__":
    Test()