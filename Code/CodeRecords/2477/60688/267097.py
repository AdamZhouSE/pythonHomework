class Myrect():
    def __init__(self,x,y,wight,hight):
        self.x=x;
        self.y=y;
        self.wight=wight;
        self.hight=hight;
def isoverlap(rect1:Myrect,rect2:Myrect):
    if rect1.x+rect1.wight<rect2.x or rect2.x+rect2.wight<rect1.x or rect1.y-rect1.hight > rect2.y or rect2.y-rect2.hight>rect1.y:
        return 0;
    else: return 1;
nums=int(input());
results=[];
for i in range(nums):
    numslist = (input().split(" "));
    numslist=list(int(x) for x in numslist);
    firstrect=Myrect(numslist[0],numslist[1],numslist[2]-numslist[0],numslist[1]-numslist[3])
    numslist = (input().split(" "));
    numslist=list(int(x) for x in numslist);
    secondrect=Myrect(numslist[0],numslist[1],numslist[2]-numslist[0],numslist[1]-numslist[3])
    temp=isoverlap(firstrect,secondrect);
    results.append(temp)
for i in results:
    print(i)