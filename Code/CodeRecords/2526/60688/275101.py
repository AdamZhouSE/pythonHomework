try:
    rownum=input();
    numlist1=eval(rownum);
except:
    print(rownum)
numlist2=eval(input());
numlist1.extend(numlist2);
numlist1.sort();
print(numlist1);