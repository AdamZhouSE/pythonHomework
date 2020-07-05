n=input().split(" ")
n=[int(x) for x in n]
k=n[1]
ls=input().split(" ")
total=0
for i in range(len(ls)):
    if ls[i].count("4")+ls[i].count("7")<=k:
        total=total+1

        
print(total)