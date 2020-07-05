numbers = input().split(",")
i=0
while i<len(numbers):
    print(numbers[i],end="")
    if i!=len(numbers)-1:
        print("/",end="")
        if i==0:
            print("(",end="")
    else:
        print(")",end="")
    i=i+1
print()