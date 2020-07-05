stra = input()
strb = input()
index =0
for i in range(len(stra)):
    for j in range(i+1,len(stra)+1):
        temp = stra[i:j]
        a = strb.count(temp)
#        print("check:{} number:{}".format(temp,a))
        index+=a
print(index,end=' ')
