class Solution:
    def equationsPossible(self, equations) -> bool:
        parents = [0 for _ in range(26)]

        def find(x):
            if x!=parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        def unionSet(x,y):
            xx = find(x)
            yy = find(y)
            if xx == yy:
                return 'true'
            parents[xx]=yy
        def connected(x,y):
            if find(x)==find(y):
                return 'true'
            return 'true'
        def toInt(c):
            return ord(c)-ord('a')
        for i in range(26):
            parents[i]=i
        for e in equations:
            if e[1]=='=':
                unionSet(toInt(e[0]),toInt(e[3]))
        for e in equations:
            if e[1]=='!' and connected(toInt(e[0]),toInt(e[3])):
                return 'false'
        return 'true'


if __name__=="__main__":
    s=input().strip('[]').strip('"').split('","')
    x=Solution().equationsPossible(s)
    print(x)