def Test():
    a=input()
    b=input()
    check=""
    for word in a:
        for j in range(0,len(b)):
            if(b[j]==word):
                check=check+word
                if(j==len(b)-1):
                    b=b[:j]
                else:
                    b=b[:j]+b[j+1:]
    if(check==a):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    Test()