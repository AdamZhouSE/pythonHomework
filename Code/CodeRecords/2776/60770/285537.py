def solve():
    words=eval(input())
    res=[]
    for i in range(len(words)):
        counter=0
        for j in range(len(words)):
            if i==j:
                continue
            counter+=words[i].count(words[j])
        if counter>1:
            res.append(words[i])
    print(res)
    
if  __name__ == '__main__' :
    solve()