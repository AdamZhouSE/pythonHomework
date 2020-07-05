word=input()
string="CODEFESTIVAL2016"
result=0
for i in range(16):
    if word[i]!=string[i]:
        result+=1
print(result)