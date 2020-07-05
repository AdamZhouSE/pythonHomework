word=raw_input()
temp=""
resu=""
for w in word:
    fi w not in temp:
        temp=temp+w
        if len(temp)>len(resu):
            res=temp
    else:
        i=temp.index(w)
        if i==len(temp)-1:
            temp=w
        else:
            temp=temp[i+1:]+w
        if len(temp)>len(resu):
            resu=temp
print(len(resu))