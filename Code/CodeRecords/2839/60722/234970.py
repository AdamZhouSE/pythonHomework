n=int(input())
nums=[]
for i in range(n):
    new=input()
    if new in nums:
        print("YES")
    else:
        print("NO")
    nums.append(new)