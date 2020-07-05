n=int(input())
for i in range(n):
    length=int(input())
    a=input()
    l=a.split(",")
    l= list(map(int, l))
    
    my_set=set([])
    sum=0
    for x in l:
        sum+=x
        if sum in my_set:
            print(Yes)
            break
        else:
            my_set.add(sum)
    if len(my_set)==length:
        print(No)
    