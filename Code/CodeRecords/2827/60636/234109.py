number=int(input(""))
list=input("").split(" ")
result=[]
for i in range(number):
    result.append(int(list[i]))
result.sort()
answer=""
for i in range(number):
    answer=answer+str(result[i])+" "
print(answer[:-1])