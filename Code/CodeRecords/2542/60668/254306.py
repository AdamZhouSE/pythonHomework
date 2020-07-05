def arrays_38_Longest(list = []):
    list = sorted(list)
    co = 0
    Max = 0
    for i in range(0,len(list)-1):
        if list[i+1]-list[i]==1:
            co+=1
        else:
            if Max<co+1:
                Max = co+1
            co = 0
    print(Max)
if __name__=='__main__':
    list = eval(input())
    arrays_38_Longest(list)