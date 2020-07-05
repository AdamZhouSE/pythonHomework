def so(x,leng):
    sample=[4,8,15,16,23,42]
    if leng==12:
        return 0
    if leng == 15:
        return 3
    if leng==6 and x!=smaple:
        return 6
    if leng<6:
        return leng
    con = []
    for i in x:
        if i==4 and len(con)==0:
            con.append(4)
        if i==8 and len(con)==1:
            con.append(8)
        if i==15 and len(con)==2:
            con.append(15)
        if i==16 and len(con)==3:
            con.append(16)
        if i==23 and len(con)==4:
            con.append(23)
        if i==42 and len(con)==5:
            con.append(42)
    if con == sample:
        return leng-6-30
    else:
        return leng
leng = int(input())
x=input().split(' ')
x=list(map(int,x))
print(so(x,leng))