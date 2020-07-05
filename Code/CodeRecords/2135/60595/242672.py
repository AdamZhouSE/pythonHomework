import math
def Test():
    nums=eval("["+input()+"]")
    x=sum(nums)/len(nums)
    part1=math.ceil(x)
    part2=math.floor(x)
    s1=0
    s2=0
    for a in nums:
        s1=s1+abs(a-part1)
        s2 = s2 + abs(a - part2)
    print(min(s1,s2))
if __name__ == "__main__":
    Test()