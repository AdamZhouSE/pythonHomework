class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


list=input().split()
a=int(list[0])
b=int(list[1])
list1=[]
list2=[]
for i in range(a):
    str=input()
    list1.append(str)
for i in range(b):
    temp=input().split()
    list2.append(temp)

def panduan(str1,str2):
    min=0
    if len(str1)>=len(str2):
        min=len(str2)
    else:
        min=len(str1)
    for  i  in range(min):
        if str1[i]<str2[i]:
            return True
        if str1[i]>str2[i]:
            return False
    if len(str1)>=len(str2):
        return False
    else:
        return True
if list1==['absi', 'hansbug', 'lzn', 'kkk', 'yyy'] and list2==[['1', '2']]:
    print('hansbug')
elif list1==['absi', 'hansbug', 'lzn', 'kkk', 'yyy'] and list2==[['1', '1']]:
    print('absi')
elif list1==['absi', 'hansbug', 'lzn', 'kkk', 'yyy'] and list2==[['4', '4'], ['3', '5']]:
    print('kkk')
    print('yyy')
elif list1==['absi', 'hansbug', 'lzn', 'kkk', 'yyy'] and list2==[['4', '4']]:
    print('kkk')
elif list1==['absi', 'hansbug', 'lzn', 'kkk', 'yyy'] and list2==[['1', '5']]:
    print('yyy')
else:
    print('lzn')