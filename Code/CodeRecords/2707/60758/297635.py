couple=eval(input())
for i in range(len(couple)):
    if couple[i]%2!=0:
        couple[i]-=1
count=0
for i in range(0,len(couple),2):
    if couple[i]!=couple[i+1]:
        count+=1
        for j in range(i+2,len(couple)):
            if couple[j]==couple[i]:
                couple[i+1],couple[j]=couple[j],couple[i+1]
                break
print(count)