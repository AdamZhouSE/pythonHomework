'''
输入一个字符串，长度小于等于200，然后将输出按字符顺序升序排序后的字符串。
'''

string = list(input())
l = len(string)
replace = string
for i in range(0,l):
    for j in range(l-1,i,-1):
        if (string[j] <= string[j - 1]):
            tmp = string[j]
            string[j] = string[j - 1]
            string[j-1] = tmp
print(''.join(str(s) for s in string))