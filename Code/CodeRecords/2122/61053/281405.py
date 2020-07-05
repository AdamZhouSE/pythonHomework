def gcd(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    print(c%gcd(a,b)==0)