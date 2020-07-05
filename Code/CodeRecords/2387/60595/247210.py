def Test():
    s=input().split()
    n=int(s[0])
    m=int(s[1])
    nums=eval("["+input().strip().replace(" ",",")+"]")
    for i in range(0,m):
        q=input().split()
        op=int(q[0])
        left=int(q[1])
        right=int(q[2])
        if(op==0):
            part=sorted(nums[left:right+1])
            nums[left:right+1]=part
        else:
            part = sorted(nums[left:right + 1],reverse=True)
            nums[left:right + 1] = part
    index=int(input())
    print(nums[index-1])
if __name__ == "__main__":
    Test()