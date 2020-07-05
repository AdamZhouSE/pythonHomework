def main():
    numOftests = int(input())
    for i in range(numOftests):
        str0 = input()
        word = input()
        sl = perm(word)
        num = 0
        for j in range(len(str0)-len(word)+1):
            for m in range(len(sl)):
                if str0[j:j+len(word)] == sl[m]:
                    num+=1
                    break
        print(num)


def perm(s=''):   #注意这些排列组合中有相同的
    # 这里是递归函数的出口，为什么呢，因为这里表示：一个长度为1的字符串，它的排列组合就是它自己。
    if len(s)<=1:
        return [s]
    sl=[] #保存字符串的所有可能排列组合
    for i in range(len(s)):  #这个循环，对应 解题思路1）确定字符串的第一个字母是谁，有n种可能（n为字符串s的长度
        for j in perm(s[0:i]+s[i+1:]): #这个循环，对应 解题思路2）进入递归，s[0:i]+s[i+1:]的意思就是把s中的s[i]给去掉
            sl.append(s[i]+j) # 对应 解题思路2）问题就从“返回字符串中的字母排列组合” **变成了** “返回 第一个字母+除去第一个字母外的字符串的排列组合”
    return sl

if __name__ == '__main__':
    main()