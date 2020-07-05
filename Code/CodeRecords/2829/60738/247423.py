n=int(input())
num_list=list(map(int,input().split(" ")))
num_list.sort()
length=len(num_list)
num1=num_list[length-1]-num_list[1]
num2=num_list[length-2]-num_list[0]
print(min(num1,num2))
    