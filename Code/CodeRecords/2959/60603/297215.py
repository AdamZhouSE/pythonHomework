stra = input()
strb = input()
count =0
for i in range(len(stra)):
    for j in range(i+1,len(stra)+1):
        temp = stra[i:j]
        a = strb.count(temp)
#        print("check:{} number:{}".format(temp,a))
        count+=a
print(count)