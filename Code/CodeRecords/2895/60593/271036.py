lr=eval(input())
ans=lr[1]
for i in range(lr[0],lr[1]):
    ans&=i
print(ans)