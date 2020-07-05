import collections
def smallestStringWithSwaps(s, pairs):
        p = {i:i for i in range(len(s))}
        def f(x):
            if x != p[x]:
                p[x] = f(p[x])
            return p[x]
        
        for i, j in pairs:
            p[f(j)] = f(i)      
        d = collections.defaultdict(list)
        for i, j in enumerate(map(f, p)):
            d[j].append(i)
        ans = list(s)
        for q in d.values():
            t = sorted(ans[i] for i in q)   
            for i, c in zip(sorted(q), t):
                ans[i] = c
        return ''.join(ans)
s=input()
str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
list1=str1.split(',')
i=0
pairs=[]
list2=[]
while i <len(list1):
    list2.append(int(list1[i]))
    list2.append(int(list1[i+1]))
    pairs.append(list2)
    i=i+2
    list2=[]
print(smallestStringWithSwaps(s, pairs))