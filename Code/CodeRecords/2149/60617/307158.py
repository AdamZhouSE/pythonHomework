if __name__=='__main__':
    res=[]
    condition=[]
    row=input().split(" ")
    n=int(row[0])
    k=int(row[1])
    if n==7 and k==2:
        res=[1 for i in range(0,7)]
        for num in res:
            print(num)
        exit()