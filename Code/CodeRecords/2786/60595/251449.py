def Test():
    n=int(input())
    nums=eval("["+input().strip().replace(" ",",")+"]")
    nums.sort()
    for i in range(1,n+1):
        temp=min(nums)
        if(i>temp):
            print(i)
            break
        else:
            nums.remove(temp)
    print(n)
if __name__ == "__main__":
    Test()