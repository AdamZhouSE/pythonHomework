def find_longest(line, k):
    ans = len(line)
    while ans >= k:
        for i in range(len(line)-ans+1):
            sub = line[i:i+ans]
            if len(set(sub)) == k:
                return ans
        ans -= 1
    return 0

def test():
    line = input()
    k = int(input())
    return find_longest(line, k)

A = []
for i in range(int(input())):
    A.append(test())

for i in A:
    print(i)