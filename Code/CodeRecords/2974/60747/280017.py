def cut(s: str):
    results = []
    num = 0
    # x + 1 表示子字符串长度
    for x in range(len(s)):
        # i 表示偏移量
        for i in range(len(s) - x):
            if results.count(s[i:i+x+1])==0:
                results.append(s[i:i + x + 1])
    return results
def back(str):
    rs=list(reversed(str))
    if list(str)==rs:
        if len(str)%2==1:
            return True
    return False
if __name__=="__main__":
    n=int(input())
    s=input()
    answer=[]
    for j in range(1,n):
        A=s[0:j]
        B=s[j:n]
        A_arr=cut(A)
        B_arr=cut(B)
        A_num=0
        B_num=0

        for i in range(len(A_arr)):
            if back(A_arr[i]):
                A_num+=1
        for j in range(len(B_arr)):
            if back(B_arr[j]):
                continue
            else:
                B_num+=1
        answer.append(A_num*B_num)
    print(max(answer))
