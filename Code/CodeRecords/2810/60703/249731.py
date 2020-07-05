n = input();
bits = max([int(x) for x in list(n)]);
ans = ["" for x in range(bits)];
for i in n:
    temp = int(i);
    for j in range(bits):
        ans[j]+="1" if temp>0 else "0";
        temp-=1;
print(bits);

if(len(ans)==1):#长度为1单独考虑
    print(int(ans[0]))
else:
    for i in range(0,len(ans)-1):
        print(int(ans[i]),end=" ");
    print(int(ans[len(ans)-1]))
