s = input()
ans=0
for i in range(int(s)+1):
    ans+=str(i).count('1')
print(ans)