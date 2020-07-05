def Test():
    s=int(input())
    printnum(s)
    print("")
def printnum(n):
    if (n>0):
        printnum(n-1)
        print(n,end=" ")
if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()