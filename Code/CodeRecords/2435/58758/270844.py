N, M = [int(x) for x in input().split()]
dic = []
for i in range(N):
    dic.append(input())
ans = []
for i in range(M):
    start, end = [int(x) for x in input().split()]
    words = dic[start-1: end]
    words.sort()
    ans.append(words[len(words)-1])
for i in ans:
    print(i)
