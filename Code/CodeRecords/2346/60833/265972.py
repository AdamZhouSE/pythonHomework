lines=[]
while True:
    try:
        lines.append(input())
    except:
        break
n=int(lines.pop(0))

for i in range(0,n):
    list1 = list(lines.pop(0).split(" "))
    list_number = list(lines.pop(0).split(" "))
    list_number = list(map(int, list_number))
    m=int(list1[0])
    n=int(list1[1])
    br=0
    bc=0
    er=m-1
    ec=n-1
    list_out=[]
    result=[]
    for k in range(0,m):
        list_in = []
        for j in range(0,n):
            list_in.append(int(list_number.pop(0)))
        list_out.append(list_in)
    while(1):
        for i in range(bc,ec+1):
            result.append(list_out[br][i])
        br=br+1
        if(br>er):
            break
        for i in range(br,er+1):
            result.append(list_out[i][ec])
        ec=ec-1
        if(ec<bc):
            break
        for i in range(ec,bc-1,-1):
            result.append(list_out[er][i])
        er=er-1
        if(er<br):
            break
        for i in range(er,br-1,-1):
            result.append(list_out[i][bc])
        bc=bc+1
        if(bc>ec):
            break
    for j in result:
        print(j,end=" ")
    print("")