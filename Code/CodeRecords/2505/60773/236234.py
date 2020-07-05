start=input()
#print(start)
list=start.split(',')
#print(list)
num=len(list)
for i in range(num):
    for j in range(i+1,len(list),1):
        #print("#")
        if(list[i]==list[j]):
            result=list[i]
            print(result)
            break
