rowstr=input();
rowlist=rowstr.split("+");
rowlist.sort();
result="";
for i in rowlist:
    result=result+i+"+";
print(result[:len(result)-1]);