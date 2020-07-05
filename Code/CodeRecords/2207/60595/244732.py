def Test():
    s=input().split()
    num=int(s[0])
    k=int(s[1])
    if(num//k>=2):
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()