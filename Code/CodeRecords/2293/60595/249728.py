def Test():
    n=int(input())
    nums = eval("[" + input().strip().replace(" ", ",") + "]")
    k=int(input())
    nums.sort()
    print(nums[k-1])
if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()