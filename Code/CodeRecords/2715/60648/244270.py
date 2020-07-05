class Solution:

    def removeStones(self, stones):

        """

        :type stones: List[List[int]]

        :rtype: int

        """

        UF = {}

        def find(x):

            if x != UF[x]:

                UF[x] = find(UF[x])

            return UF[x]

        

        def union(x, y):

            UF.setdefault(x, x)

            UF.setdefault(y, y)

            UF[find(x)] = find(y)



        for i, j in stones:

            union(i, ~j)

        return len(stones) - len({find(x) for x in UF})



if __name__ == "__main__":
    
    stones=input().strip('[]').split("], [")


    stones=[i.split(",") for i in ls]
     

    print(Solution().removeStones(stones))