out=""
result=[]
index=-1
for _ in range(int(input())):
    op=input()
    do=op[0]
    word=op[2]
    if do=='T':
        out+=word
        result.append(out)
        index+=1
    elif do=='U':
        out=result[index-int(word)]
        index=index-int(word)
    elif do=='Q': 
        print(out[int(word)-1])