try:
    rownum=input();
    numlist1=eval(rownum);
    rownum2=input();
    numlist2 = eval(rownum2);
    numlist1.extend(numlist2);
except:
    print(rownum)
    print(rownum2)

numlist1.sort();
print(numlist1);