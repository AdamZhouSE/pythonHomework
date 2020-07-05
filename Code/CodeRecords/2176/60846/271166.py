# def cmpMethod(a,b):
#     if a[0]>b[0]: return 1
#     if a[0]<b[0]: return -1
#     if a[1]<b[1]: return 1
#     if a[1]>b[1]: return -1

# if __name__=='__main__':
str=input()
chars=[]
for ch in str:
    chars.append(ch)
charsWithIdx=[]
for idx,ch in enumerate(chars):
    charsWithIdx.append((ch,idx+1))
#print(charsWithIdx)
from operator import itemgetter
charsWithIdx.sort(key=itemgetter(1),reverse=True)
charsWithIdx.sort(key=itemgetter(0))
#print(charsWithIdx)
firstCh=False
for element in charsWithIdx:
    if not firstCh:
        print(element[1],end='')
        firstCh=True
    else:print('',element[1],end='')
print()