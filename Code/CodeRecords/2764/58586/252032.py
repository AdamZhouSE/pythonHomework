nums=int(input())
for i in range(nums):
    num=int(input())
    def backtrack(num):
        if num==0:
            return 0
        if num==1:
            return 1
        if num==2:
            return 2
        return max(num,backtrack(num//2)+backtrack(num//3)+backtrack(num//4))
    print(backtrack(num))