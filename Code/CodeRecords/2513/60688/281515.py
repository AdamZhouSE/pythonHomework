gaps=int(input());
numlist=[];
for _ in range(gaps):
    temp="["+input()+"]";
    temp=eval(temp);
    numlist.append(list(int(i) for i in temp));
keynum=int(input());
numslist=[];
for _ in range(len(numlist)):
    numslist.extend(numlist[_]);
numslist.sort();
print(numslist[keynum-1])