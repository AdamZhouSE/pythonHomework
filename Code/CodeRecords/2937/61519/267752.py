word=raw_input()
string="CODEFESTIVAL2016"
list1=list(word)
list2=list(string)
out=16
for i in range(16):
    if list1[i]==list2[i]:
        out=out-1
print(out)