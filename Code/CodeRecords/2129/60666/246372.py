n=int(input())
temp={n}
count=0
while 1 not in temp:
    temp={j for i in temp for j in [[i//2],[i+1,i-1]][i&1]}
    count+=1
print(count)