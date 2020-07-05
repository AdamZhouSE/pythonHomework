def Test():
    num=int(input())
    print(Deal(num))

def Deal(x):
    if(x==1):
        return chr(64+x)
    else:
        return Deal(x-1)+chr(64+x)+Deal(x-1)


if __name__ == "__main__":
    Test()