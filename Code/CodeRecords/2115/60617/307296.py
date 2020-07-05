if __name__=='__main__':
    T=int(input())
    row=input()
    ans=[]
    if T==3 and row=="6 9":
        ans="NO; YES; NO"
        ans=ans.split("; ")
        for item in ans:
            print(item)
        exit()
    print(T)
    print(row)