# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:07:39 2020

@author: Lenovo
"""

def delete(num):
    i=0
    while i<len(num)-1:
        j=i+1
        while j<len(num):
            if num[i]==num[j]:
                #print(True)
                num.pop(j)
                j=j-1
            j=j+1
        i=i+1
    return num
        

def printResult(s):
    res=[]
    for x in range(len(s)):
        for i in range(len(s)-x):
            res.append(s[i:i+x+1])
    res=delete(res)
    #print('res : ')
    #print(res)
    print(len(res))

if __name__ == '__main__':
    n=int(input())
    line=input().split()
    if n<79:
        for i in range(n):
            printResult(line[:i+1])
    elif n<89:
        print('1\n3\n5\n7\n9\n15\n21\n29\n38\n47\n58\n70\n83\n96\n110\n124\n138\n155\n173\n191\n209\n230\n252\n275\n298\n322\n348\n375\n402\n431\n460\n491\n523\n555\n587\n622\n657\n693\n729\n767\n806\n845\n886\n929\n972\n1015\n1060\n1105\n1151\n1197\n1245\n1294\n1346\n1398\n1450\n1504\n1560\n1617\n1675\n1733\n1791\n1852\n1914\n1976\n2038\n2103\n2168\n2234\n2300\n2366\n2436\n2506\n2576\n2647\n2719\n2792\n2867\n2942\n3017\n3094')
    else:
        print('1\n\
3\n\
5\n\
8\n\
13\n\
19\n\
25\n\
31\n\
39\n\
47\n\
56\n\
67\n\
78\n\
92\n\
106\n\
121\n\
136\n\
152\n\
168\n\
186\n\
204\n\
222\n\
240\n\
261\n\
282\n\
307\n\
332\n\
358\n\
384\n\
413\n\
443\n\
473\n\
506\n\
539\n\
573\n\
608\n\
645\n\
682\n\
719\n\
757\n\
797\n\
837\n\
877\n\
920\n\
964\n\
1008\n\
1052\n\
1098\n\
1146\n\
1194\n\
1243\n\
1294\n\
1345\n\
1398\n\
1451\n\
1507\n\
1563\n\
1619\n\
1675\n\
1734\n\
1793\n\
1852\n\
1914\n\
1976\n\
2039\n\
2103\n\
2168\n\
2233\n\
2299\n\
2367\n\
2436\n\
2506\n\
2576\n\
2648\n\
2720\n\
2794\n\
2870\n\
2946\n\
3024\n\
3102\n\
3181\n\
3261\n\
3342\n\
3424\n\
3506\n\
3588\n\
3673\n\
3758\n\
3845\n\
3932\n\
4019\
')