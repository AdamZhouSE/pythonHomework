def Test():
    s=int(input())
    for i in range(0,100):
        z=bin(s)
        if(z.count("1")==1):
            print(s)
            break
        s=s+1

if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()