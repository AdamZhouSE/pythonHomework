def Test():
    x=int(input())
    nums=eval("["+input().split(" ",",")+"]")
    sum=0
    for num in nums:
        sum=sum+abs(num-1)
    print(sum)
if __name__ == "__main__":
    Test()