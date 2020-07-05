def search(ls,t):
    for i in range(len(ls)):
        if ls[i]==t:
            return i
        else:
            continue
    return -1


if __name__=="__main__":
    ls=input().strip('[]').split(",")
    ls=[int(ls[i]) for i in range(len(ls))]
    t=input()
    t=int(t)
    x=search(ls,t)
    print(x)