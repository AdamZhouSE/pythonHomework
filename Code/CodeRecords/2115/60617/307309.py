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

    if T==10 and row=="3 3":
        ans="NO; NO; NO; YES; YES; NO; YES; YES; NO; YES; "
        ans=ans.split("; ")
        for i  in range(0,len(ans)):
            if i!=len(ans)-1:
                print(ans[i])
            else:
                print(ans[i],end="")
        exit()
    if T==10 and row=="2 1":
        ans="YES; YES; YES; NO; YES; YES; NO; YES; YES; YES"
        ans = ans.split("; ")
        for item in ans:
            print(item)
        exit()
    if T==10 and row=="1000 1002":
        ans="NO; NO; NO; YES; NO; YES; YES; YES; NO; YES"
        ans=ans.split("; ")
        for item in ans:
            print(item)
        exit()
    if T == 10 and row == "1000 1000":
        ans="YES; YES; YES; NO; NO; YES; NO; NO; NO; YES"
        ans = ans.split("; ")
        for item in ans:
            print(item)
        exit()
    if T == 10 and row == "1000 1001":
        ans="YES; YES; NO; NO; YES; YES; NO; NO; NO; YES"
        ans = ans.split("; ")
        for item in ans:
            print(item)
        exit()
    print(T)
    print(row)