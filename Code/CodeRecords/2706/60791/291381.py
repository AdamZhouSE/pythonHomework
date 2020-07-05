acc = eval(input())
res = []
done = [0]*len(acc)
for i in range(len(acc)):
    if(done[i] == 1):
        pass
    else:
        temp = acc[i]
        for x in range(i+1,len(acc)):
            re = False
            for index in range(1,len(acc[x])):
                if acc[x][index] in temp:
                    
                    done[x] = 1
                    re = True
                    break
            if re:
                for index in range(1,len(acc[x])):
                    if acc[x][index] not in temp:
                        temp.append(acc[x][index])
        
        res.append(temp)
print(res)
