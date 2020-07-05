tests=(int)(input())
for i in range(0,tests):
    result = ''
    nums=(int)(input())
    record=0
    k=1
    start=1
    while(record<nums):
        for j in range(0,k):
            result+=str(start)+" "
            record+=1
            if(record==nums):
                break
            start += 2
        k+=1
        start-=1
    print(result[:len(result)-1])