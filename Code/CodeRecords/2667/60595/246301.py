def Test():
    s=input().split()
    i=int(s[0])
    l=int(s[1])
    print(pow(2,l)-i)


if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()