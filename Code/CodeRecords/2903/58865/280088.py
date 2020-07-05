str_arr=eval(input())

def occurOnce(s):
    '''判断字符串每个字母是否只出现了一次'''
    return 1 if len(set(s))==len(s) else 0

def subSetBin(arrlen):
    '''返回集合长度的01序列 列表'''
    arr=[]
    for i in range(1<<arrlen):
        s=''
        for j in range(arrlen):
            if(1<<j)&i:
                s+='1'
            else:
                s+='0'
        arr.append(s)
    return arr

arr=[]
for i in subSetBin(len(str_arr)):
    s=''
    for j in range(len(i)):
        if i[j]=='1':
            s+=str_arr[j]
    arr.append(s)

arr=[len(i) for i in arr if occurOnce(i) ]
print(max(arr))

