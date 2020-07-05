times=int(input());
results=[];
for _ in range(times):
    nums= input();
    numslist = (input().split(" "));
    numslist=list(int(x) for x in numslist);
    temp=[];
    for i in range(len(numslist)-1):
        if numslist[i]>numslist[i+1]:
            temp.append(str(numslist[i+1]));
        else:temp.append("-1");
    temp.append("-1");
    results.append(" ".join(temp));
for i in results:
    print(i,end='');
    print(' ')

    