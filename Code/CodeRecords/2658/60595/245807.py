def Test():
    s=input().split()
    n=int(s[0])
    x=int(s[1])
    nums=eval("["+input().strip().replace(" ",",")+"]")
    result=[]
    for i in range(1,n+1):
        for j in range(0,n):
            if(i+j<=n):
                sum=0
                for k in range(j,j+i):
                    sum=sum|nums[k]
                if(sum%x==0):
                    result.append(sum)
    if(result):
        print(max(result))
    else:
        print(0)
        print(s,nums)


if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()