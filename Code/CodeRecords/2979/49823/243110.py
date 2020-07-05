def a(s):
    l=s.split(' ')
    index=0
    for i in range(1,len(l)):
        if len(l[i])>len(l[index]):
            index=i
    print(l[index]) 
if __name__=='__main__':
    a(input())