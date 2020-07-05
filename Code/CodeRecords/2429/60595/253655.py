def Test():
    n=int(input())
    nums=eval("["+input().strip().replace(" ",",")+"]")
    print(max(nums)-min(nums))
if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()