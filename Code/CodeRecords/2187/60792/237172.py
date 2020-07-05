def max_sum(line,k):
    sum=0
    for i in range(0,len(line)-k+1):
        temp_sum=0
        for j in range(0,k):
            temp_sum=temp_sum+int(line[i+j])
        if temp_sum>sum:
            sum=temp_sum
    return sum

    
number=int(input())
for i in range(0,number):
    n,k=map(int,input(). strip().split())
    line=[n]
    line=input().split(" ")
    print(max_sum(line,k))
    