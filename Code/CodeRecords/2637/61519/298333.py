word=list(input())
tem=[]
for i in range(1,len(word)-1):
    if word[i]!=",":
        tem.append(word[i])
for i in range(1,len(tem)-1):
    if tem[i]>tem[i-1] and tem[i]>tem[i+1]:
        print(i)
        break