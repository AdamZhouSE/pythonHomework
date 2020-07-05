numbers=list(map(int,input()[1:-1].split(",")))
for i in range(0,len(numbers)):
    if i%2==0:
        if numbers[i]!=numbers[i+1]:
            print(numbers[i])
            break