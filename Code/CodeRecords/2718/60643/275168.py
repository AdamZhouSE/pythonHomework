import collections

def solution(s: str, pairs: [int]) -> str:
    p = {i: i for i in range(len(s))}  # 初始化并查集
    def find(x):
        if p[x]==x:
            return x
        else:
            return find(p[x])

    for i, j in pairs:
        root1=find(i)
        root2=find(j)
        p[root2] = root1
        # 合并可交换位置
    d = collections.defaultdict(list)
    temp=list(map(find, p))#再一次 以消除没找完全的情况 得到temp,temp数组里是所有数字都完全查找到根节点
    for i, j in enumerate(temp):
        d[j].append(i)
    # 排序
    ans = list(s)
    for q in d.values():
        t = sorted(ans[i] for i in q)
        for i, c in zip(sorted(q), t):
            ans[i] = c
    return ''.join(ans)


if __name__=="__main__":
    s=input()
    pairs=eval(input())
    # 初始化并查集
    p = [i for i in range(len(s))]
    ans=solution(s,pairs)
    print(ans)