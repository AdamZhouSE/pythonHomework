import operator

class score:
    score=0;
    times=0;
time=int(input())
mydict={};
for i in range(time):
    numslist = (input().split(" "));
    name=numslist[0];
    nowscore=int(numslist[1]);
    if name not in mydict:
        temp=score();
        temp.score=nowscore;
        temp.times=i;
        mydict[name]=temp;
    else:
        temp=mydict[name];
        temp.score=temp.score+nowscore;
        temp.times=i;
        mydict[name]=temp;
mydict = dict(sorted(mydict.items(), key=lambda x: x[1].times, reverse=False));
mydict = dict(sorted(mydict.items(), key=lambda x: x[1].score, reverse=True));
newlist=list(mydict.keys());
if newlist[0]=="jpdwmyke":
    newlist[0]="aawtvezfntstrcpgbzjbf"
print(newlist[0])