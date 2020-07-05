def maxLength(arr):
    t=[]
    for i in arr:
        if len(i)==len(set(i)):
            t.append(i)
    arrs=t[:]

    def dfs(i,cur):
        if i>=len(arrs):
            return len(cur)
        if not(set(cur)&set(arrs[i])):
            return max(dfs(i+1,cur+arrs[i]),dfs(i+1,cur))
        else:
            return dfs(i+1,cur)
    lens=dfs(0,'')
    return lens

s=input()
s=s[1:len(s)-1]
s=s.replace('"',' ')
s=s.replace(',',' ')
l=s.split()
print(maxLength(l))