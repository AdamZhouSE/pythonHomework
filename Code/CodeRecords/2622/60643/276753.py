if __name__=="__main__":
    lst=eval(input())
    st=set(lst)
    floor=len(lst)//2
    ans=[]
    for i in st:
        n=lst.count(i)
        if n>floor:
            ans.append(i)
    ans=[str(x) for x in ans]
    print(",".join(ans))