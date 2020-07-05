a= int(input())
count = 0
for i in range(0,100):
    count +=pow(4,i)
    if(count==a-1):
        print(True)
        break
    
    if(count==a):
        print(True)
        break
    if(count>a):
        print(False)
        break
