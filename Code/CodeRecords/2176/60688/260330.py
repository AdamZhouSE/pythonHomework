stringrow=input();
strings={};
for i in range(len(stringrow)):
    temp=stringrow[i:];
    strings[temp]=i;
# stringlists=sorted(strings,key=lambda x:x[0],reverse=True);
stringlists = dict(sorted(strings.items(), key=lambda item:item[0],reverse=True))

results=list(stringlists.values());
for i in range(len(results)):
    results[i]=str(results[i]+1)
results.reverse();
result=" ".join(results);
print(result)