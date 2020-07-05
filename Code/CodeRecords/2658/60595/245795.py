def Test():
    s=input().split()
    n=int(s[0])
    x=int(s[1])
    nums=eval("["+input().strip().replace(" ",",")+"]")
    print(s)
    print(nums)

if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()