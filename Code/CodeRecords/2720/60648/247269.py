class Solution:
    def makeConnected(self, n: int, connections) -> int:
        if len(connections) < n - 1:
            return -1
        p = [[i] for i in range(n)]
        for x, y in connections:
            if p[x] is not p[y]:
                if len(p[x]) < len(p[y]):
                    x, y = y, x
                p[x].extend(p[y])
                for z in p[y]:
                    p[z] = p[x]
        return len({*map(id, p)}) - 1


if __name__=="__main__":
    #ls=[]
    s=input()
    s=int(s)
    pairs=input().strip('[]').split('],[')
    pairs=[i.split(",") for i in pairs]
    for i in range(len(pairs)):
        for j in range(2):
            pairs[i][j]=int(pairs[i][j])
    #print(pairs)
    x=Solution().makeConnected(s,pairs)
    print(x)