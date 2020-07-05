n = input()
bits = max([int(x) for x in list(n)])
ans = [""]*bits
for i in n:
    temp = int(i)
    for j in range(bits):
        ans[j]+="1" if temp>0 else "0"
        temp-=1
print(bits)
ans = [bin(int(x,2))[2:] for x in ans]
print(" ".join(ans))