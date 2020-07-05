def Test():
    s=int(input())
    two=bin(s)[2:]
    one=two.count("1")
    print("odd" if one%2==1 else "even")

if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()