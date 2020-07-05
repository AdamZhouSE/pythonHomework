def to_int(l):
    for i in range(len(l)):
        l[i] = int(l[i])
    return l


limit = to_int(input().split(" "))
nums = to_int(input().split(" "))
for i in range(limit[1]):
    op = input().split(" ")
    if op[0] == "Q":
        sub = []
        for j in range(int(op[1])-1, int(op[2])):
            sub.append(nums[j])
        sub.sort()
        print(sub[int(op[3])-1])
    else:
        op[1] = int(op[1])
        op[2] = int(op[2])
        nums[op[1]-1] = op[2]