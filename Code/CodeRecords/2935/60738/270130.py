letter_list=list(input())
length=len(letter_list)
amount=0
for i in range(length):
    if letter_list[i]=="Q":
         for j in range(i,length):
                if letter_list[j]=="A":
                    for k in range(j,length):
                        if letter_list[k]=="Q":
                            amount+=1
print(amount,end="")

    
    