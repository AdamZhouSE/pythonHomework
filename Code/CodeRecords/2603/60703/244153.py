import re;
import sys;
List = re.split(',|\]|\[',input());
List = List[1:len(List)-1];
ListNum = [int(x) for x in List];
Num = sys.maxsize;
for i in range(0,len(ListNum)):
    for j in ListNum[:i]:
        if(abs(ListNum[i]-j))<Num:
            Num=abs(ListNum[i]-j);


print(Num);