string1=input()
string2=input()
amount=0
length1=len(string1)
length2=len(string2)
for i in range(length1):
    for j in range(i+1,length1+1):
        for k in range(length2):
            for t in range(k+1,length2+1):
                if string1[i:j]==string2[k:t]:
                    amount+=1
print(amount)
                