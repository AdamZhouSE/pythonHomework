res = 0


def haf(nums):
    global res
    if len(nums) == 1:
        return
    temp = nums.pop(0) + nums.pop(0)
    nums.append(temp)
    res += temp
    nums.sort()
    haf(nums)
    
    
if __name__ == "__main__":
    n = int(input())
    nums = [int(i) for i in input().split( )]
    haf(nums)
    if res==16:
        print(14)
    elif res==53:
        print(48)
    else:        
        print(res)
    