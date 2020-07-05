def isSimilar(a:str,b:str):
    length=len(a)
    diff=0
    for i in range(length):
        if a[i]!=b[i]:
            diff+=1
    if diff==2 or diff==0:
        return True
    return False

def union(root1,root2):
    if root1!=root2:
        Parent[root2]=root1#注意赋值的左右次序

#找爸爸  parent数组不同索引位置的值可以拥有同一个爸爸的下标
def find(x):
    if Parent[x]==-1:
        return x
    return find(Parent[x])


if __name__=="__main__":
    words=eval(input())
    total_len=len(words)
    Parent=[-1]*total_len#存放的是爸爸的索引
    #将相似单词组相连 即放到一个并查集里面  每个独立的并查集根节点的值都是-1
    for i in range(total_len):
        for j in range(i+1,total_len):
            root1=find(i)
            root2=find(j)
            if root1==root2:
                continue
            if isSimilar(words[i],words[j]):
                union(root1,root2)

    ans=0
    for i in range(total_len):
        if Parent[i]==-1:
            ans+=1
    print(ans)