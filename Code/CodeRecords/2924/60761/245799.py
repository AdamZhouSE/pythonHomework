n,r,avg=map(int,input().split(" "))
grades=[]
essays=[]
write_esy=0
for i in range(n):
    ai,bi=map(int,input().split(" "))
    grades.append(ai)
    essays.append(bi)
needGrd=n*avg-sum(grades)
while(needGrd>0):
    j=r-grades.pop(essays.index(min(essays)))
    if(needGrd>j):
        needGrd=needGrd-j
    else:
        j=needGrd
        needGrd=0
    write_esy+=min(essays)*j
    essays.remove(min(essays))
print(write_esy)
