def numSimilarGroups(A):
    visited = set()
    count = 0
    stack = []
    N = len(A)
    M = len(A[0])
    if N > 2*M:
        A_set = set(A)
        for word in A:
            if word not in visited:
                stack.append(word)
                count += 1
            while stack:
                cur = stack.pop()
                visited.add(cur)
                for i in range(M - 1):
                    for j in range(i + 1, M):
                        if cur[i] !=cur[j]:
                            new = cur[:i] + cur[j] + cur[i + 1:j] + cur[i] + cur[j+1:]
                            if new not in visited and new in A_set:
                                stack.append(new)
        return count
    for i in range(N):
        if A[i] not in visited:
            stack.append(A[i])
            count +=1
        while stack:
            word = stack.pop()
            visited.add(word)
            for j in range(i + 1, N):
                newword = A[j]
                if newword not in visited:
                    diff = []
                    for idx in range(M):
                        if word[idx] != newword[idx]:
                            diff.append(idx)
                        if len(diff) > 2:
                            break
                    if len(diff) == 2:
                        a, b = diff
                        if word[a] == newword[b] and word[b] == newword[a]:
                            stack.append(newword)
                            
    return count

s=input()
s=s[1:len(s)-1]
sl=s.split(',')
l=[]
for x in sl:
    l.append(x[1:len(x)-1])
print(numSimilarGroups(l))