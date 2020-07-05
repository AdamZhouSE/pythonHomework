reference='CODEFESTIVAL2016'
actual=input()
count=0
for i in range(len(reference)):
    if reference[i]!=actual[i]:
        count=count+1
print(count)