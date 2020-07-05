sstr =bin(int(input()))
dstr = ""
for i in range(2,len(sstr)):
    dstr = dstr + ("1" if sstr[i:i+1]=="0" else "0")

print(int(dstr,2))