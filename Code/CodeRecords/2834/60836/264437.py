"""
一个班级的学生写了一份只有选择题的测试
这个班有 n 个学生。测试有 m 个问题
每个问题都有 5 个可能的答案 (A, B, C, D或E)，每个问题都有一个正确的答案
问题 i 的正确答案值 ai 分，不正确的答案得零分。
学生们记得他们在考试中给出的答案，但是他们不知道正确的答案是什么
他们非常乐观，所以他们想知道班上所有学生的最大可能总分是多少
"""

nm=[int(m) for m in str(input()).split(" ")]
n=nm[0]
m=nm[1]

answer=[]
for i in range(n):
    answer.append(list(str(input())))

score=[int(m) for m in str(input()).split(" ")]

total_score=0
for i in range(m):
    A_num = 0
    B_num = 0
    C_num = 0
    D_num = 0
    E_num = 0
    for m in range(n):
        if answer[m][i]=='A':
            A_num+=1
        elif answer[m][i]=='B':
            B_num+=1
        elif answer[m][i] =='C':
            C_num+=1
        elif answer[m][i] =='D':
            D_num+=1
        else:
            E_num+=1

    total_score+=max(A_num,B_num,C_num,D_num,E_num)*score[i]

print(total_score)