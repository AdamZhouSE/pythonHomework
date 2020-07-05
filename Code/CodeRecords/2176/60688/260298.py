stringrow=input();
strings={};
for i in range(len(stringrow)):
    temp=stringrow[i:];
    strings[temp]=i;
stringlists=sorted(strings,key=lambda x:x[0],reverse=True);
# stringresult=list(strings.values())
results=[];
for i in range(len(stringlists)):
    results.append(str(strings[stringlists[i]]+1));
results.reverse();
result=" ".join(results);
print(stringrow)