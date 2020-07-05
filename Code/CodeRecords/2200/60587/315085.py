s = input()
nums = input()
k = int(input())
res = 0
lst = []
for i in range(0, len(s)):
    for j in range(i + 1, len(s) + 1):
        tmp = nums[i:j]
        # print(tmp)
        count = 0
        for m in range(0, len(tmp)):
            if tmp[m] == '0':
                count += 1
            if count > k:
                break
        if count <= k:
            boolean = True
            for p in lst:
                if p == tmp:
                    boolean = False
                    break
            if boolean:
                lst.append(tmp)
                # print(lst)
                res += 1
        else:
            continue
print(res)
