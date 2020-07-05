def Test():
    q=int(input())
    s=str(bin(q))
    if(s.count("1")==1):
        print("True")
    else:
        print("False")
if __name__ == "__main__":
    Test()