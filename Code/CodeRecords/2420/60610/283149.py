num=int(input())
result=[]
for i in range(1,num//2+1):
    mid=[i,num-i];
    if("0" not in str(i))&("0" not in str(num-i)):
        result.append(mid)
        break;
print(result[0])