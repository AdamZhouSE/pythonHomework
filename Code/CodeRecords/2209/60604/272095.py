x=int(input())
s=input()
tmp=[]
for I in range(x):
    tmp.append(input())
    #print(tmp[-1])
maxL=0
dic=[]
L=[]
for I in tmp:
    L.append(len(I))
for i in range(x):
    max=0
    if L[i]>max:
        max=i
i=0
res=0
while(i<len(300000)):
    j=0#在所有单词及L中的下标
    if 