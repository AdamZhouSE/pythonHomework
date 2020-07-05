def Test():
    s=int(input())
    two=bin(s)[2:]
    new=int(("0"+two.replace("0","1")),2)
    print(str(new-s)+" "+str(new))
    
if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()