arr=eval(input())
counter=1
while(True):
    if(arr.count(counter)==0):
        print(counter)
        break
    counter+=1