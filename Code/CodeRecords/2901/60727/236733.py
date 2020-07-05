a= int(input())
count = 0
count1=0
for i in range(0,100):
    count +=pow(4,i)
    count1+=pow(4,i+1)
    
    if(count==a or count1==a):
        print(True)
        break
    if(count>a and count1 >a):
        print(False)
        break
