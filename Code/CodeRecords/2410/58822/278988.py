#def dp(a, num):
#    max_len = 1
#    for i in range(len(a)):
#        tmp_len = 1
#        for j in range(i + 1, len(a)):
#            if a[j] - a[i] == tmp_len * num:
#                tmp_len += 1
#        max_len = max(max_len, tmp_len)
#    return max_len


#if __name__ == '__main__':
#    a = list(eval(input()))
#    print(dp(a, int(input())))
n=input()
b=list(eval(n))
num=int(input())
max=1
if num==0:
    for i in range(len(b)):
        index=i
        jian=1
        if(index+1==len(b)):
            break
        while(b[index]==b[index+1]):
            jian=jian+1
            if(jian>max):
                max=jian
            index+=1
            if (index+1)==len(b):
                break
    print(max)
    exit()
jian=1
k=0
for i in range(len(b)):
    k=b[i]
    if((k+num) in b[i+1:len(b)]):
        for r in range(i+1,len(b)):
            while((k+num) == b[r]):
                if(b[r]==(k+num)):
                    jian += 1
                    del b[r]
                    b.insert(r,-77)
                    k=k+num
        if(jian>max):
            max=jian
    jian=1
print(max)
