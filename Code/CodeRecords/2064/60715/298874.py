s=(input(""));
result=0;
list={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000};
for i in range(len(s)-1):
    if list[s[i]]<list[s[i+1]]:
        result-=list[s[i]];
    else:
        result+=list[s[i]];
result+=list[s[-1]];
print(result);
