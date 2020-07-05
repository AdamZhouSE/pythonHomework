def cou(num):
    count = 0
    for a in range(len(num) - 2):
        for b in range(a + 1, len(num) - 1):
            for c in range(b + 1, len(num)):
                if num[a] + num[b] == num[c] or num[a] + num[c] == num[b] or num[b] + num[c] == num[a]:
                    count += 1
    if count==0:
        return -1
    else:
        return count
T=int(input())
while T>0:
    n=int(input())
    num=[int(n) for n in input().split()]
    print(cou(num))
    T-=1