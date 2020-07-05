l = list(input())
l2 = []
for i in range(len(l)):
    s="".join(l[0:i])+"".join(l[i:len(l)])
    l2.append(s)
l2.sort()
print(l2[len(l2)-1])