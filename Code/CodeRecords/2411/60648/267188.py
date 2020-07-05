class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        return all((coordinates[1][1] - coordinates[0][1]) * (coordinates[i][0] - coordinates[0][0]) == (coordinates[i][1] - coordinates[0][1]) * (coordinates[1][0] - coordinates[0][0]) for i in range(2, len(coordinates)))

    
if __name__=="__main__":
    n=int(input())
    ls=[]
    for i in range(n):
        s=input().split(',')
        s=[int(s[i]) for i in range(len(s))]
        ls.append(s)
    x=Solution().checkStraightLine(ls)
    print(x)