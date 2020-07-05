num=int(input())
for i in range(num):
    list=[]
    num_=int(input())
    for j in range(num_+1):
        if j&num_==j:
            list.append(j)
    for j in range(len(list)):
        print(list[-1-j],end=" ")
    print()