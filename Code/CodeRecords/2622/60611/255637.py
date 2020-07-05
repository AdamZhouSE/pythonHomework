from collections import Counter

source=eval(input())
l=set(source)
dic=Counter(source)
for ele in l:
    if dic[ele]>len(source)/2:
        print(ele)