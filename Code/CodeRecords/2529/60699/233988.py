n=int(input())
temp=str(n).split()
temp.sort()
for i in range(0,32):
    k=2**i
    if len(temp)!=len(str(k)):
        continue
    str_temp=str(k).split()
    if str_temp==temp:
        print(True)
        break
    if(i==31):
        print(False)