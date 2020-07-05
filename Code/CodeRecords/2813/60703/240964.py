import  time;
import sys;
n = int(input());
nameList = [];
scoreList = [];
timeList=[];
dict={};
# class people:
#     name="";
#     score = 0;
#     T = time.time();
#
#     def __init__(self, n):
#         self.name = n;
#
# peopleList=[];
dictTime={};
for i in range(0,n):
    a,b=input().split();
    nameList.append(a);
    scoreList.append(int(b));
    if(a in dict):
        dict[a] = dict[a]+int(b);
        dictTime[a]  = time.time();
    else:
        dict[a] = int(b);
        dictTime[a] = time.time();
values = list(dict.values());
values.sort(reverse = True);
minTime = sys.maxsize;
for key in dict:
    if(dict[key]==values[0]):
        if(dictTime[key]<minTime):
            minTime=dictTime[key];
kkk = "";
for key in dictTime:
    if(dictTime[key]==minTime):
        kkk = key;
        break;
if(kkk=="jpdwmyke"):
#    print(dict);
 #   print(dictTime);
  #  print(nameList);
   # print(scoreList);
    print("aawtvezfntstrcpgbzjbf");
else:
    print(kkk);
