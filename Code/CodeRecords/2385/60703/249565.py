n = int(input());
numlist=[];
#找规律发现是斐波那契,即前面一项以0结尾的数为m，以1结尾的为k；
#只要2m+k即可。 即m + （m+k）//m+k为前面一项总数
#m为前面第二项总数。（都加了0变成前面一项）
for i in range(0,n):
    numlist.append(int(input()));
fibonci =[];
maxNum = max(numlist);
fibonci.append(0);
fibonci.append(2);
fibonci.append(3);
for i in range(0,maxNum+1):
    fibonci.append(0);
for i in range(3,maxNum+1):
    fibonci[i] = fibonci[i-1]+fibonci[i-2];

for i in range(0,len(numlist)):
    print(fibonci[numlist[i]]);