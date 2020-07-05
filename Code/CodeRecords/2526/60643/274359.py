def process_inp(s):
    s = s[1:len(s)-1]
    lst=s.split(",")
    res=[]
    for i in range(len(lst)):
        if lst[i].isdigit():
            res.append(int(lst[i]))
        elif len(lst[i])>0:
            if lst[i][0]=='-':
                res.append(int(lst[i]))
    return res

if __name__=="__main__":
    s1=input()
    s2=input()
    lst1=process_inp(s1)
    lst2=process_inp(s2)
    ans=lst1+lst2
    print(sorted(ans))