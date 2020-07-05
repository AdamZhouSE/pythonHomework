source=input()[1:-1]
assist=list(map(int,source.split(",")))
assist=sorted(assist)
tag=0
for i in range(1,len(assist)+1):
    if not(i in assist):
        print(i)
        tag=1
        break
if tag==0:
    print(assist[-1]+1)