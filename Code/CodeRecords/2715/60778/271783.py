stones=eval(input())
i=0
move=0
while(stones):
    move+=1
    tmp=stones[0]
    stones.remove(tmp)
    count_row=0
    count_list=0
    for i in stones:
        if(i[0]==tmp[0]):
            count_row+=1
        elif(i[1]==tmp[1]):
            count_list+=1
    else:
        for i in stones:
            if(i[0]==tmp[0] and count_list>count_row):
                stones.remove(i)
            elif(i[1]==tmp[1] and count_list<=count_row):
                stones.remove(i)
print(move)