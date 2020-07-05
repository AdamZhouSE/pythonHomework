def Test():
    n=int(input())
    nums=eval("["+input().strip().replace(" ",",")+"]")
    print(check(nums))
def check(nums):
    save=[]
    for q in nums:
        if(save.count(q)!=0):
            return q
        else:
            save.append(q)
    return -1


if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()