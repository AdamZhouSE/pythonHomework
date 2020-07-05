num = int(input())
for i in range(num):
    Len_list=list(input())
    Str_list=input().split()
    S1=Str_list[0]
    S2=Str_list[1]
    count=0
    S1_position=0
    S2_position=0
    for S1_index in range(len(S1)-1):
        S1_position = S1_index
        if S1[S1_index]==S2[S2_position]:
            S2_position = S2_position + 1
            count=count+1
            for S2_index in range(S2_position-1,len(S2)-1):
                if S1[S1_position+1]==S2[S2_index+1]:
                    S1_position=S1_position+1
                    S2_position=S2_position+1
                else:
                    break
            S1_index=S1_position
            if S2_position==len(S2):
                S2_position=0

    if S1[S1_position]==S2[S2_position]:
        count=count+1
    print(count)