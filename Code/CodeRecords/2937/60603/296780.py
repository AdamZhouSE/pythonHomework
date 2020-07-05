stan="CODEFESTIVAL2016"
string=input()
count=0
for i in range(len(string)):
    if(string[i]!=stan[i]):
        count+=1
print(count)