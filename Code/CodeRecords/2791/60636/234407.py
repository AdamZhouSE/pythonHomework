number=int(input(""))
list=input("").split(" ")
stage=[]
for i in range(number):
    stage.append(int(list[i]))
times=0
location=0
result=[]
for i in range(number):
    if(i==number-1):
        times=times+1
        result.append(number-location)
        location=number
    else:
        if(stage[i+1]==1):
            times=times+1
            result.append(i-location+1)
            location=i+1
print(times)
answer=""
for i in result:
    answer=answer+str(i)+" "
print(answer[:-1])