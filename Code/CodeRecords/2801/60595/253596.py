import itertools
def Test():
    n=int(input())
    nums=eval("["+input().strip().replace(" ",",")+"]")
    if(len(nums)<3):
        print("NO")
    elif(len(nums)==3):
        print("YES" if check(nums[0],nums[1],nums[2]) else "NO")
    else:
        property=list(itertools.combinations(nums,3))
        isOK=False
        for x in property:
            temp=list(x)
            if(check(temp[0],temp[1],temp[2])):
                isOK=True
        if(isOK):
            print("YES")
        else:
            print("NO")

def check(a,b,c):
    if(a+b>c or a+c>b or b+c>a):
        return True
    return False
if __name__ == "__main__":
   Test()