A=[int(a) for a in input().split(",")]
n1 = A.count(1)
if not n1:
    print([0, len(A) - 1])
elif n1 % 3 or len(A) < 3:
    print([-1, -1])
else:
    split_num = n1 // 3

    split_list = []
    while len(split_list) < 3:
        start = j = 0
        for i in range(len(A)):
            if A[i]:
                if not j:
                    start = i
                j += 1
                if j == split_num:
                    split_list.append((start, i))
                    start = j = 0

    s1, s2, s3 = split_list[0], split_list[1], split_list[2]
    zero_num = len(A) - split_list[-1][1] - 1
    if A[s1[0]:s1[1 ] +1] != A[s2[0]:s2[1 ] +1] or A[s1[0]:s1[1 ] +1] != A[s3[0]:s3[1 ] +1]:
        print("[-1, -1]")

    elif not(s2[0 ] -s1[1] > zero_num and s3[0 ] -s2[1] > zero_num):
        print("[-1, -1]")
    else:
        
        print([s1[1 ] +zero_num, s2[1 ] +zero_num +1])
