class Solution :
    def spot(self):
        n = int(input())
        coordinates = []
        Slope = []
        deSlope = []
        maxNum = 0
        for i in range(n) :
            coord = input()
            coordinates.append(coord)
        for o in range(n-1) :
            for j in range(o+1, n) :
                slope = coordinates[j][1] - coordinates[o][1] / coordinates[j][0] - coordinates[o][0]
                Slope.append(slope)
        Slope.sort()
        deSlope.append(1)
        for i in range(Slope.__len__()-1) :
            if Slope[i] != Slope[i+1] :
                deSlope.append(1)
            else :
                deSlope[-1] += 1
        deSlope.sort()
        print(deSlope[-1]+1)
solution = Solution()
solution.spot()