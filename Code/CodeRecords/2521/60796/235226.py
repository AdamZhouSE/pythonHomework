barcodes=input()
barcodes=barcodes[1:len(barcodes)-1]
ls=[]
ls=barcodes.split(",")
ls=[int(x) for x in ls]
for i in range(0,len(ls)-1):
    if ls[i]==ls[i+1]:
        for j in range(0,len(ls)):
            if j==0 or j==len(ls)-1:
                if ls[j]!=ls[i] :
                    break
            else:
                if ls[j]!=ls[i] and ls[j-1]!=ls[j+1]:
                    break  #把ls[j]插入ls[i+1]的位置
        a=ls[j]
        del ls[j]
        if j<i:
            ls.insert(i,a)
        else:
            ls.insert(i+1,a)
print(ls)
