
def num_subsequences(seq, sub):
    if not sub:
        return 1
    elif not seq:
        return 0
    result = num_subsequences(seq[1:], sub)
    if seq[0] == sub[0]:
        result += num_subsequences(seq[1:], sub[1:])
    return result
k=int(input())
for i in range(k):
    input()
    list1=input().split(' ')
    str=list1[0]
    subList=list1[1]
    print(num_subsequences(str,subList))