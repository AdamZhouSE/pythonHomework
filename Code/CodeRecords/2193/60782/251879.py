'''
题目描述
人的一生不仅要靠自我奋斗，还要考虑到历史的行程。

历史的行程可以抽象成一个 01 串，作为一个年纪比较大的人，你希望从历史的行程中获得一些姿势。

你发现在历史的不同时刻，不断的有相同的事情发生。比如，有两个人同时在世纪之交 11 年的时候上台，同样喜欢与洋人谈笑风生，同样提出了以「三」字开头的理论。

你发现，一件事情可以看成是这个 01 串的一个前缀，这个前缀最右边的位置就是这个事情的结束时间。

两件事情的相似度可以看成，这两个前缀的最长公共后缀长度。

现在你很好奇，在一段区间内结束的事情中最相似的两件事情的相似度是多少呢？

输入描述
第一行两个整数n、m,表示串长和询问个数。
第二行长度为n的01串，表示历史的行程。
接下来m行,每行两个正整数l、r表示询问的区间,包括端点，保证1≤l< r≤n。
输出描述
输出m行，对每个询问输出一个整数表示最大的相似度。
测试样例
样例1:输入-输出-解释
4 2
0101
1 3
2 4

1
2
'''
def longest_prefix(str1,str2):
    ans = min(len(str1),len(str2))
    for i in range(0,ans):
        if str1[i] != str2[i]:
            ans = i
            break
    return ans

def find_max_prefix(strs):
    strs = sorted(strs)
    ans = 0
    for i in range(0,len(strs)-1):
        ans = max(ans,longest_prefix(strs[i],strs[i+1]))
    return ans

n,m = map(int,input().split(" "))
string = input()

ans = []
for i in range(0,m):
    l,r = map(int,input().split(" "))
    str = []
    for end in range(l,r+1):
        str.append(string[0:end][::-1])
    ans.append(find_max_prefix(str))
for no in ans:
    print(no)


