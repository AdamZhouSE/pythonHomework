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
print(sources)
blood=[]
for i in range(len(sources)):
    bloods=[]
    for j in range(len(sources[i])):
        bloods.append(0)
    blood.append(bloods)
for i in range(len(sources)):
    for j in range(len(sources[i])):
        if i==0 and j==0:
            blood[i][j]=sources[0][0]
        elif i==0:
            blood[i][j]=sources[0][j]+blood[i][j-1]
        elif j==0:
            blood[i][j]=sources[i][0]+blood[i-1][j]
        else:
            blood[i][j]=sources[i][j]+max(blood[i-1][j],blood[i][j-1])
print(blood[len(blood)-1][len(blood[len(blood)-1])-1])
    