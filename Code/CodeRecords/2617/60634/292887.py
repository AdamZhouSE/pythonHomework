#main-----
test = int(input())
for t in range(test):
    temp = input().split(' ')
    s = temp[0]
    k = int(temp[1])
    
    mem = [0 for x in range(len(s))]
    count = 0
    
    l = 1
    while l <= len(s):
        i = 0
        while i <= len(s)-l:
            if s[i+l-1] == '1':
                mem[i] += 1
            if mem[i] == k:
                count += 1
            i += 1
        l += 1
    print(count)

























