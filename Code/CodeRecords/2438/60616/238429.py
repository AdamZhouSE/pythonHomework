colors=input()
blue=colors.count('2')
red=colors.count('0')
white=colors.count('1')
ans=[]
for i in range(red):
    ans.append(0)
for i in range(white):
    ans.append(1)
for i in range(blue):
    ans.append(2)
print(ans)