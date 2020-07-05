first=eval(input().replace("i","j"))
second=eval(input().replace("i","j"))
result:complex=first*second
res="";
if result.real==0.0:
    res="0+"+str(result).replace("j","i");
else:
    res=str(int(result.real))+"+"+str(result.imag).replace("j","i");
print(res)