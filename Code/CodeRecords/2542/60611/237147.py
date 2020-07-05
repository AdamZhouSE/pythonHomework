source = str(input())[1:-1]
assist=list(map(int,source.split(",")))
count=1
assist=sorted(assist)
for i in range(-1,-len(assist),-1):
    assist[i]=assist[i]-assist[i-1]
for i in range(1,len(assist)):
    if assist[i]==1:
        count+=1
print(count)