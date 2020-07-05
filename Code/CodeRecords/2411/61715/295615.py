class Solution :
    def Sameline():
        n = int(input())
        coordinates = []
        for i in range(n) :
            coord = input()
            coordinates.append(coord)
        Slope = (int(coordinates[1][1]) - int(coordinates[0][1])) / (int(coordinates[1][0]) - int(coordinates[0][0]))
        for o in range(n-1) :
            slope = (int(coordinates[o+1][1]) - int(coordinates[o][1])) / (int(coordinates[o+1][0]) - int(coordinates[o][0]))
            if slope != Slope :
                print(False)
                return 0
        print(True)
    Sameline()