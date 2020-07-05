'''
题目描述

给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。

输入描述

第一行一个字符串，第二行一个字符串字典。所有输入的字符串只包含小写字母。字典的大小不会超过 1000。所有输入的字符串长度不会超过 1000。
输出描述

找到的字符串。
测试样例

样例1: 输入-输出-解释

abpcplea
["ale","apple","monkey","plea"]
apple
'''

def find(word):
    tempString=string
    for char in word:
        if char not in tempString:
            return False
        else:
            index=tempString.index(char)
            tempString=tempString[index+1:]
    return True





if __name__ == '__main__':
    string=input()
    arr=eval(input())

    arr.sort(key=lambda x:len(x),reverse=True)
    temp=[]
    for i in range(0,len(arr)-1):
        if len(arr[i])==len(arr[i+1]):
            temp.append(arr[i])
        elif temp!=[]:
            temp.sort(key=lambda x:x[0])
            firstIndex = i - (len(temp) - 1)
            for k in range(0, len(temp)):
                arr[firstIndex + k] = temp[k]
    if temp!=[]:
        temp.sort(key=lambda x: x[0])
        firstIndex = i - (len(temp) - 1)
        for k in range(0, len(temp)):
            arr[firstIndex + k] = temp[k]

    for word in arr:
        if find(word):
            print(word)
            break
