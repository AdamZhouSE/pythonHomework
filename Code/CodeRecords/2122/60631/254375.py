a=int(input())
b=int(input())
c=int(input())
def canMeasureWater(x: int, y: int, z: int):  
        import math
        if x + y < z: return False
        if x == z or y == z or x + y == z: return True
        return z % math.gcd(x, y) == 0
print(canMeasureWater(a,b,c))