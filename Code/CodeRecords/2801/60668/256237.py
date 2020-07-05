def arrays_41_triangle(list = []):
    co = 0
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            for k in range(j+1,len(list)):
                if list[i]+list[j]>list[k] and list[j]+list[k]>list[i] and list[k]+list[i]>list[j]:
                    co+=1
    if co >0:
        print("YES")
    else:
        print("NO")
if __name__=='__main__':
    n = input()
    list = [int(i) for i in input().split()]
    arrays_41_triangle(list)