n=input().split(" ")
lens=[]
for i in range(len(n)):
    lens.append(len(n[i]))
print(n[lens.index(max(lens))])