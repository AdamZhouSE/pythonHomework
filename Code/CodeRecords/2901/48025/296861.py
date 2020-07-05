n=int(input())
str_bin=str(bin(n))[2:len(str(bin(n)))]
result=True
for i in range(0,len(str_bin)-1):
    if(str_bin[i]==str_bin[i+1]):
        result=False;
        break;
print(result)
    