def Test():
    n=int(input())
    map={}
    result={}
    names=[]
    a=[]
    maxvalue=-203049
    for i in range(0,n):
        s=input().split()
        names.append(s[0])
        a.append(int(s[1]))
        try:
            map[names[i]]+=a[i]
        except:
            map[names[i]]=a[i]
    for i in range(0,n):
        maxvalue=max(maxvalue,map[names[i]])
    for i in range(0,n):
        try:
            result[names[i]]+=a[i]
        except:
            result[names[i]]=a[i]
        if (result[names[i]] >= maxvalue and map[names[i]] >= maxvalue):
            print(names[i])
            break
if __name__ == "__main__":
    Test()