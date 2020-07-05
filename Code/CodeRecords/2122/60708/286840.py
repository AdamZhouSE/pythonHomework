def canMeasureWater(x,y,z) :
    if z==0:
        return True
    return  (x + y >= z and z % gcd(x, y) == 0);
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
if __name__ == '__main__':
    x=int(input())
    y=int(input())
    z=int(input())
    print(canMeasureWater(x,y,z))