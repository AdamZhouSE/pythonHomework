def Test():
    s=int(input())
    two=bin(s)[2:]
    zero=two.count("0")
    one=two.count("1")
    print(zero^one)

if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()