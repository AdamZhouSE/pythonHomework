def Test():
    n=int(input())
    nums=eval("["+input().strip().replace(" ",",")+"]")
    nums.sort()
    result=n
    for i in range(1,n+1):
        temp=min(nums)
        if(i>temp):
            result=i
            print(nums)
            break
        else:
            nums.remove(temp)
    print(result)
if __name__ == "__main__":
    Test()