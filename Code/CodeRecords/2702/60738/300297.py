string_list=[]
while(True):
    try:
        string_list.append(list(map(int,input())))
    except:
        break
wid=len(string_list)
leng=len(string_list[0])
res=0
for i in range(wid):
    for j in range(leng):
        if string_list[i][j]==1:
            