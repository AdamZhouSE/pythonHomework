n=int(input())
temp=str(n).split()
temp.sort()
for i in range(0,33):
    k=2**i
    str_temp=str(k).split()
    if str_temp==temp:
        print("true")
        break
    if(i==31):
        print("false")