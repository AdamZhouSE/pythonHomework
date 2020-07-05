from sys import stdin

def has_equal_1_2_0(str):
    return str.count('0')==str.count('1') and str.count('0')==str.count('2')

num=int(stdin.readline().strip())
for i in range(0,num):
    str=stdin.readline().strip()
    count=0
    for j in range(3,len(str)):
        se=[]
        for k in range(0,len(str)-j+1):
            if has_equal_1_2_0(str[k:k+j]):
                se.append(str[k:k+j])

        count+=len(se)
    print(count)