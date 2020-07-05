
class Solution :
    def Boomerang():
        n = int(input())
        coordinates = []
        for i in range(n):
            coord = input()
            coordinates.append(coord)
        coordinates.sort()
        slope0 = coordinates[1][1] - coordinates[0][1] / coordinates[1][0] - coordinates[0][0]
        slope1 = coordinates[2][1] - coordinates[0][1] / coordinates[2][0] - coordinates[0][0]
        if slope0 == slope1 :
            return False
        if coordinates[0] == coordinates[1] or coordinates[1] == coordinates[2] :
            return False
        return True
    print(Boomerang())