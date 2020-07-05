s=input("");
num_tuple=[1000,500,100,50,10,5,1];
roman_tuple=['M','D','C','L','X','V','I'];
list=dict(zip(roman_tuple,num_tuple));
result=0;
for i in range(len(s)-1):
    if list[s[i]]<list[s[i+1]]:
        result-=list[s[i]];
    else:
        result+=list[s[i]];
result+=list[s[-1]];
print(result);

