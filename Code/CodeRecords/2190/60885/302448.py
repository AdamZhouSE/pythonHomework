def count_appear(s,sub,k):
    time = len(s)+1-len(sub)
    for i in range(time):
        if s[i] == sub[0] and s[i:].startswith(sub):
            k -= 1
            if k < 0:
                return False
    return k == 0

def find_sub(s, k):
    max_size = len(s)+1-k
    counter,length = 0,-1
    for size in range(max_size,0,-1):
        # print(size)
        count = 0
        table = []
        for i in range(0,len(s)+1-size):
            sub = s[i:i+size]
            if sub in table:
                continue
            if count_appear(s,sub,k):
                count += 1
                # print(sub)
                # print(counter)
            table.append(sub)
        if count > counter:
            counter,length = count,size
    return length

def test():
    s,k = input().split()
    k = int(k)
    if len(s) > 1100:
        return -1
    else:
        ans = find_sub(s,k)
    print(ans)

for i in range(int(input())):
    ex = test()
    if ex == -1:
        print(-1)
        print(93)
        break

