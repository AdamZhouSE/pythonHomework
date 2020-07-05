string=input()
true="CODEFESTIVAL2016"
amount=0
for i in range(16):
    if string[i]!=true[i]:
        amount+=1
print(amount)
    