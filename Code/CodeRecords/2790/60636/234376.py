number=input("").split(" ")
list_a=input("").split(" ")
list_b=input("").split(" ")
a=[]
b=[]
result=[]
for i in range(int(number[0])):
    a.append(int(list_a[i]))
for i in range(int(number[1])):
    b.append(int(list_b[i]))
for b_i in b:
    sum=0
    for a_i in a:
        if(a_i<=b_i):
            sum=sum+1
    result.append(sum)
answer=""
for sum_0 in result:
    answer=answer+str(sum_0)+" "
print(answer[:-1])