def Test():
    gray="0000"+bin(int(input()))[2:]
    b=""
    b=b+gray[0]
    for i in range(1,len(gray)):
        b=b+xor(gray[i],b[i-1])
    print(int(("0b"+b),2))

def xor(a,b):
    return "0" if a==b else "1"

if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()