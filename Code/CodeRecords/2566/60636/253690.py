n=int(input())
sources=[]
try:
    while(True):
        x=input().split(",")
        source=[]
        for i in x:
            source.append(int(i))
        sources.append(source)
except(EOFError):
    pass
blood=[]
for i in range(len(sources)):
    bloods=[]
    for j in range(len(sources[i])):
        bloods.append(0)
    blood.append(bloods)
for i in range(len(sources)-1,-1,-1):
    for j in range(len(sources[i])-1,-1,-1):
        if i==len(sources)-1 and j==len(sources[i])-1:
            blood[i][j]=-sources[i][j]
        elif i==len(sources)-1:
            blood[i][j]=-sources[i][j]+blood[i][j+1]
        elif j==len(sources[i])-1:
            blood[i][j]=-sources[i][j]+blood[i+1][j]
        else:
            blood[i][j]=-sources[i][j]+max(min(blood[i+1][j],blood[i][j+1]),1)
print(blood)
    