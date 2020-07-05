n=int(input())
prime_list=[2,3,5,7,11,14,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
def prime(m):
    for i in range(2,int(m/2)):
        if m%i==0:
            return False
    return True
chushu_list=[]
for i in range(len(prime_list)-1):
    for j in range(i+1,len(prime_list)):
        chushu_list.append(prime_list[i]*prime_list[j])
for k in range(n):
    N=int(input())
    chushu_list.sort()
    for w in chushu_list:
        if (N%w==0):
            if(prime(int(N/w))):
                print(1)
                break
            else:
                print(0)
                break
        if w>=167:
            print(0)
            break