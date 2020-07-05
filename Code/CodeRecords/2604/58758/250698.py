inp = input()
strs = inp[2: len(inp)-2].split('", "')
target = ord(input())
if ord(strs[len(strs)-1]) <= target:
    print(strs[0])
else:
    for i in strs:
        if ord(i) > target:
            print(i)
            break
