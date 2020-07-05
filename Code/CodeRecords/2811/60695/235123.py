#print("input p and n(:p n):")
s = input()
p = int(s.split(" ")[0])
n = int(s.split(" ")[1])
nums = [None]*n
space = [None]*p
flag = True

#print("input the n numbers to insert:")
for i in range(0, n):
    nums[i] = int(input())
for i in range(0, n):
    mod = nums[i] % p
    if space[mod] is None:
        space[mod] = nums[i]
    else:
        print(i+1)
        flag = False
        break
if flag:
    print(-1)