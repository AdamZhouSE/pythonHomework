import itertools
def Test():
    n,k=map(int,input().split())
    nums=[]
    for i in range(0,k):
        s=eval("["+input().strip().replace(" ",",")+"]")
        nums.append(s)
    print(check(nums))
def check(nums):
    i=len(nums[0])
    while(i>1):
        all=list(itertools.combinations(nums[0],i))
        for p in all:
            if(has(list(p),nums)):
                return i
        i=i-1
    return 1
def has(p,nums):
    for i in range(0,len(nums)):
        temp=nums[i]
        save=p.copy()
        for k in range(0,len(temp)):
            if(not save):
                break
            if(temp[k]==save[0]):
                save.remove(save[0])
        if(save):
            return False
    return True
if __name__ == "__main__":
    Test()