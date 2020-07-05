test=input()
test=test[1:len(test)-1].split(",")
result=int(test[0])
for i in range(int(test[0])+1,int(test[1])+1):
    result=result&i
print(result)