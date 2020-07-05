def solve(number,list):
    length=[]
    for i in range(number):
        length.append(int(list.split(" ")[i]))

    for i in range(number,0,-1):
        sum=0
        for j in range(number):
            if(length[j]>=i):
                sum=sum+1
        if(sum>=i):
            return i
test_number=int(input(""))
list=[]
for i in range(test_number*2):
    list.append(input(""))
for i in range(0,test_number*2,2):
    print(solve(int(list[i]),list[i+1]))