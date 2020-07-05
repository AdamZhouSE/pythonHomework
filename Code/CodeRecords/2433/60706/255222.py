str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
i=0
list1=str1.split(',')
list2=[]
seq=[]
i=0
while i<len(list1):
    list2.append(int(list1[i]))
    list2.append(int(list1[i+1]))
    seq.append(list2)
    i=i+2
    list2=[]
seq = sorted(seq)
i = 1 
while i < len(seq):
    if seq[i][0] >= seq[i-1][0] and seq[i][0] <= seq[i-1][1]:
        if seq[i][1] <= seq[i-1][1]:
            seq.remove(seq[i])
        else:
            seq[i-1] = [seq[i-1][0], seq[i][1]]
            seq.remove(seq[i])
    else:
        i += 1
print(seq)