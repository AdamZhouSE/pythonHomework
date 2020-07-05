
if __name__ == '__main__':
    n = int(input())
    nums = [0 for i in range(100000)]
    for i in range(n):
        [a,b,h]=[int(a) for a in input().split()]
        for j in range(a,b):
            if nums[j]<h:
                nums[j]=h
    print(sum(nums))
