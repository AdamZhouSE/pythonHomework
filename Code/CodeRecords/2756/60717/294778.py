n=int(input())
red=eval(input())
blue=eval(input())
list1=[-1 for i in range(0,n)]
list1[0]=0
list2=['e']
for i in range(1,n):
    tmp='n'
    for j in range(0,i):
        if list2[j]=='e':
            if [j,i] in red:
                if list1[i]>list1[j]+1 or list1[i]<0:
                    list1[i]=list1[j]+1
                    tmp='r'
            if [j,i] in blue:
                if list1[i]>list1[j]+1 or list1[i]<0:
                    list1[i]=list1[j]+1
                    tmp='b'
        elif list2[j]=='b':
            if [j,i] in red:
                if list1[i]>list1[j]+1 or list1[i]<0:
                    list1[i]=list1[j]+1
                    tmp='r'
        elif list2[j]=='r':
            if [j,i] in blue:
                if list1[i]>list1[j]+1 or list1[i]<0:
                    list1[i]=list1[j]+1
                    tmp='b'
    list2.append(tmp)
print(list1)