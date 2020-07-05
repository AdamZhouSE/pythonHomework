t = int(input().strip())
for ind in range(t):
    li = input().strip().split(" ")
    string = li[0]
    k = int(li[1])
    result = 0
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            s = string[i:j]
            if s.count("1") == k:
                result += 1
    print(result)
