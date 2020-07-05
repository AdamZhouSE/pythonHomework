if __name__=="__main__":
    lst=input().split(",")
    k=int(input())
    lst=[int(x) for x in lst]
    lst=sorted(lst,reverse=True)
    print(lst[k-1])