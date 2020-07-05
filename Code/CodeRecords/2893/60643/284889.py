if __name__=="__main__":
    data=eval(input())
    st=set(data)
    target=0
    for i in st:
        if data.count(i)==1:
            target=i
            break
    print(target)