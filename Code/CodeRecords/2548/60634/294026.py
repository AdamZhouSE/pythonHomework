test = int(input())
for t in range(test):
    s = input()
    k = int(input())
    
    count = 0
    
    mem = [{'#'} for x in range(len(s))]
    l = 1
    while l <= len(s):
        i = 0
        while i <= len(s)-l:
            if s[i+l-1] not in mem[i]:
                mem[i].add(s[i+l-1])
            if len(mem[i])-1 == k and count < l:
                count = l
            i += 1
        l += 1
    print(count)






































