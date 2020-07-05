nums = input().split(' ')
lenth = input().split(' ')
ga = input().split(' ')
ga.sort()
gb = input().split(' ')
gb.sort()
num1 = ga[int(lenth[0])-1]
num2 = gb[int(nums[1])-int(lenth[1])]
if num1 < num2:
    print("YES")
else:
    print("NO")
