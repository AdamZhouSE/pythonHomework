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