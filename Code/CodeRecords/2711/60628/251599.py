def findSimilarGroups(A):
    visited = set()
    count = 0
    for word in A:
        if word not in visited:
            count+=1
            dfs(A,word,visited)
    return count

def dfs(A,word,visited):
    visited.add(word)
    for str in A:
        if str not in visited and isSimilar(word,str):
            dfs(A,str,visited)

def isSimilar(str1,str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count+=1
            if count>2:
                return False
    return True

inp = eval(input())
print(findSimilarGroups(inp))