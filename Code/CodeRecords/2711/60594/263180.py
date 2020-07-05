so=eval(input())
panduan=[]
jishu=0
while len(so)!=0:
    jishu+=1
    dele=[so[0]]
    while len(dele)!=0:
        xt=[]
        for index1 in range(len(so)):
            same=0
            for index2 in range(len(dele[0])):
                if so[index1][index2]==dele[0][index2]:
                    same+=1
            if same==2:
                xt.append(so[index1])
        for j in xt:
            dele.append(j)
        so.remove(dele[0])
        del(dele[0])

print(jishu)