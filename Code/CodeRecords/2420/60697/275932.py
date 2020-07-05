num=int(input())
for i in range(1,num):
    if '0' in str(i) or '0' in str(num-i):
        continue
    else:
        ans=[i,num-i]
        break
print(ans)