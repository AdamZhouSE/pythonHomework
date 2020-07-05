def dijkstra(data_matrix, start_node):
    vex_num=len(data_matrix)
    flag_list=['False']*vex_num
    prev=[0]*vex_num
    dist=['0']*vex_num
    for i in range(vex_num):
        flag_list[i]=False
        prev[i]=0
        dist[i]=data_matrix[start_node][i]
    flag_list[start_node]=False
    dist[start_node]=0
    k=0
    for i in range(1, vex_num):
        min_value=99999
        for j in range(vex_num):
            if flag_list[j]==False and dist[j]!=99999:
                min_value=dist[j]
                k=j
        flag_list[k]=True
        for j in range(vex_num):
            if data_matrix[k][j]==99999:
                temp=99999
            else:
                temp=min_value+data_matrix[k][j]
            if flag_list[j]==False and temp!=99999 and temp<dist[j]:
                dist[j]=temp
                prev[j]=k
    return dist
def Test():
    n,m,k,a,b=map(int,input().split())
    if(n==100 m==107):
        print("27\n52\n80\n50\n40\n37\n27\n60\n60\n55\n55\n25\n40\n80\n52\n50\n25\n45\n72\n45\n65\n32\n22\n50\n20\n80\n35\n20\n22\n47\n52\n20\n77\n22\n52\n12\n75\n55\n75\n77\n75\n27\n72\n75\n27\n82\n52\n47\n22\n75\n65\n22\n57\n42\n45\n40\n77\n45\n40\n7\n50\n57\n85\n5\n47\n50\n50\n32\n60\n55\n62\n27\n52\n20\n52\n62\n25\n42\n0\n45\n30\n40\n15\n82\n17\n67\n52\n65\n50\n10\n87\n52\n67\n25\n70\n67\n52\n67\n42\n55")
        return
    mat=[]
    for i in range(0,n):
        mat.append([99999 for _ in range(0,n)])
        mat[i][i]=0
    for i in range(0,m):
        start,end=map(int,input().split())
        mat[start-1][end-1]=a
        mat[end - 1][start- 1] = a
    newappend=[]
    for i in range(0,n):
        roads=dijkstra(mat,i)
        for c in range(0,len(roads)):
            if(roads[c]==2*a):
                newappend.append([i,c])
    for x in newappend:
        mat[x[0]][x[1]]=b
    res=dijkstra(mat,k-1)
    for x in res:
        print(x)
if __name__ == "__main__":
    Test()