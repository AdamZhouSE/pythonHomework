ans=[]
words=list(map(str,input()[2:-2].split('","')))
for i in range(len(words)):
    for j in range(i+1,len(words)):
        if(len(words[i]+words[j])==len(set(words[i]+words[j]))):
            ans.append(len(words[i])*len(words[j]))
print(max(ans))