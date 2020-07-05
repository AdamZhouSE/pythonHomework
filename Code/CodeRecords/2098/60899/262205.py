a = int(input())
list0 = []
while a>0:
    list0.append(a%26)
    a//=26
list0.reverse()
for i in range(len(list0)-1):
    if list0[i]==1 and list0[i+1]==0:
        list0[i] =26
        del list0[i+1]
for x in list0:
    print(chr(ord('A')+x-1),end="")
print()