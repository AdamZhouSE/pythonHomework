def find(lst,length,string):
    if length==1:
        lst.append(string+'4')
        lst.append(string+'7')
    else:
        find(lst,length-1,string+'4')
        find(lst,length-1,string+'7')

for i in range(int(input())):
    n=int(input())+1
    binary=bin(n)[2:]
    bits=len(binary)-1
    index=int(binary[1:],2)
    lst=[]
    find(lst,bits,'')
    print(lst[index])