n,m=map(int,input("").split(" "))
j=k=0
rows=[]
for i in range(n):
    rows.append(input(""))
for row in rows:
    if "B" in row:
        j=int(row.count("B")/2)+row.index("B")+1
        k=int(rows.count(row)/2)+rows.index(row)+1
        break
print(str(k)+" "+str(j))