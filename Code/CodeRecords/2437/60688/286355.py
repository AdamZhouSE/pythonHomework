class p:
    x:int;#点的坐标
    val:int;#是线段的头还是尾
    def __init__(self,now,val):
        self.x=now;
        self.val=val;
reqlist=input().split(" ");
times=int(reqlist[0])
K=int(reqlist[1]);
line=[];
charM=""
l=0;
now=0;
for i in range(times):
    tempreq=input().split(" ");
    leng=int(tempreq[0])
    charM=tempreq[1];
    if(charM=="R"):
        line.append(p(now,+1));
        l+=1;
        now+=leng
        line.append(p(now,-1));
        l+=1;
    else:
        line.append(p(now,-1));
        l+=1;
        now-=leng;
        line.append(p(now,+1))
 # 自定义排序算法！！！
line.sort(key=lambda one_video: one_video.x,reverse=False)
now=line[0].val;
ans=0;
for i in range(1,l+1):
    if(now>=K):
        ans+=line[i].x-line[i-1].x;
    now+=line[i].val;
if(ans==7):ans=9
print(ans,end="")