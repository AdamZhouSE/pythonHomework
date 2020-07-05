def isSimilar(s,x):
    if(len(x)!=len(s)):return False
    if(x==s):return True
    diff=[]
    for i in range(len(s)):
        if(s[i]!=x[i]):
            diff.append(i)
    if(len(diff)==2):
        temp=s[:diff[0]]+s[diff[1]]+s[diff[0]+1:diff[1]]+s[diff[0]]+s[diff[1]+1:]
        if(temp==x):return True
    return False

def find(parent,x):
    if(parent[x]==x):return parent[x]
    return find(parent,parent[x])

def union(parent,x,y):
    x_root=find(parent,x)
    y_root=find(parent,y)
    if(x_root!=y_root):
        parent[x_root]=y_root

inp=input()
words=inp[2:-2].split("\",\"")
parent=[i for i in range(len(words))]
for i in range(len(words)):
    for j in range(i,len(words)):
        if(isSimilar(words[i],words[j])):
            union(parent,i,j)
print (sum(parent[x]==x for x in range(len(words))))