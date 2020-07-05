import math
def Test():
    a = int(input())
    nums = eval("[" + input().strip().replace(" ", ",") + "]")
    nums.sort()
    i = -1
    while (i >= -len(nums)):
        temp = nums[i]
        try:
            if(int(math.sqrt(temp))!=math.sqrt(temp)):
                print(temp)
                break
        except:
            print(temp)
            break
if __name__ == "__main__":
    Test()
    