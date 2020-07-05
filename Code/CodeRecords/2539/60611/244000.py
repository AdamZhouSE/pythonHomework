source=input()[1:-1]
assist=list(map(int,source.split(",")))
assist2=sorted(assist)
front=0
back=0
for i in range(len(assist)):
    if assist[i]==assist2[i]:
        front=front+1
    else:
        break
for i in range(len(assist)-1,-1,-1):
    if assist[i]==assist2[i]:
        back=back+1
    else:
        break
print(len(assist)-front-back)