def numop32():

    str_in=input().split(',')
    A=[int(x) for x in str_in]

    ones = A.count(1)
    A_len = len(A)
    tag1,tag2=0,0
    if not ones:
        res= [0, A_len - 1]
    if ones % 3 != 0:
        res= [-1, -1]
    else:
        ones_in1p=ones/3
        cnt=0
        cnt_zero_p3,cnt_zero_p2,cnt_zero_p1=0,0,0
        part3,part1,part2='','',''
        for i in range(A_len-1,-1,-1):
            part3=part3+str(A[i])
            if(A[i]==1):
                cnt+=1
            if(cnt==ones_in1p):
                tag2=i
                cnt=0
                break
        for i in range(A_len - 1, -1, -1):
            if(A[i]==0):
                cnt_zero_p3+=1
            else:break
        for i in range(tag2-1, -1, -1):
            part2 = part2 + str(A[i])
            if (A[i] == 1):
                cnt += 1
            if (cnt == ones_in1p):
                tag1 = i
                cnt=0
                break
        for i in range(tag2 - 1, -1, -1):
            if(A[i]==0):
                cnt_zero_p2+=1
            else:break

        for i in range(tag1 - 1, -1, -1):
            if(A[i]==0):
                cnt_zero_p1+=1
            else:break

        if(cnt_zero_p2<cnt_zero_p3 or cnt_zero_p1<cnt_zero_p3):
            res=[-1,-1]
        else:res=[tag1-(cnt_zero_p1-cnt_zero_p3)-1,tag2-(cnt_zero_p2-cnt_zero_p3)]
    print(res)
    return 0


numop32()