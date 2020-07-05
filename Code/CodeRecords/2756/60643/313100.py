def solution(n,red,blue):
     red_path=[set() for i in range(n)]
     blue_path=[set() for i in range(n)]
     for beg,end in red:
         red_path[beg].add(end)
     for beg,end in blue:
         blue_path[beg].add(end)
     dist=[[-1]*n for _ in range(2)]#dist[0]为红蓝红顺序找到的最短距离，dist[1]为蓝红蓝找到的最短距离
     dist[0][0]=0
     dist[1][0]=0
     now_red=[0]
     now_blue=[0]#index
     steps=0
     while len(now_red)!=0 or len(now_blue)!=0:
         nxt_lvl_red=[]
         next_lvl_blue=[]
         steps+=1
         if now_red:
             for beg in now_red:
                 ends_in_blue=blue_path[beg]
                 if len(ends_in_blue)==0:
                     continue
                 for end in ends_in_blue:
                     if dist[0][end]==-1:
                         dist[0][end]=steps
                         next_lvl_blue.append(end)
         if now_blue:
             for beg in now_blue:
                 ends_in_red=red_path[beg]
                 if len(ends_in_red)==0:
                     continue
                 for end in ends_in_red:
                     if dist[1][end]==-1:
                         dist[1][end]=steps
                         nxt_lvl_red.append(end)
         now_blue=next_lvl_blue
         now_red=nxt_lvl_red

     res=[-1]*n
     for i in range(n):
         res[i]=max(dist[1][i],dist[0][i])
     return  res


if __name__=="__main__":
     n=int(input())
     red=eval(input())
     blue=eval(input())
     res=solution(n,red,blue)
     print(res)