def Test():
    s=int(input())
    print((pow(2,s+1)+pow(-1,s))/2)

if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()