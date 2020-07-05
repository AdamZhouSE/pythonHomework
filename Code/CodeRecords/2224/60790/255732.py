str1=input()
nul=[]
for num in str1:
    nul.append(int(num))
_max=max(nul)
i_max=nul.index(_max)
temp=nul[0]
nul[0]=_max
nul[i_max]=temp
for i in nul:
    print(i,end="")
print()