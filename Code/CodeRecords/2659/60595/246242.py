def Test():
    s=input().split()
    n=int(s[0])
    x=int(s[1])
    print(-(n-x)-1)


if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()