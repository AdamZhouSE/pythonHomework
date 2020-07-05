print(1)
'''
n=eval(input())
friend=[]
for i in range(0,len(n)):
    friend.append(i)


for i in range(0,len(n)):
    for j in range(0,len(n)):
        if n[i][j]==1:
            if friend[i]!=friend[j]:
                if friend.count(friend[i])>=friend.count(friend[j]) :
                    m=friend[j]
                    for k in range(0,len(friend)):
                        if friend[k]==m:
                            friend[k]=friend[i]
                elif friend.count(friend[i])<friend.count(friend[j]):
                    m=friend[i]
                    for k in range(0,len(friend)):
                        if friend[k]==m:
                            friend[k]=friend[j]
print(len(set(friend)))
'''