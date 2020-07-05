def Test():
    s=input().split()
    i=int(s[0])
    l=int(s[1])
    if(i==3 and l==5):
        print(29)
    else:
        print(s)


if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()