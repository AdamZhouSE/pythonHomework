import re;
rownum=input();
rownumres=re.sub(r",null","",rownum)
numlist1=eval(rownumres);
rownum2=input();
rownumres2=re.sub(r",null","",rownum2)
numlist2 = eval(rownumres2);
numlist1.extend(numlist2);
numlist1.sort();
print(numlist1);