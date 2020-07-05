def arrays_26_Code(n,i,sum,list = []):
    if(i==n):
        return sum % 360 == 0
    return arrays_26_Code(n,i+1,sum+list[i],list) or arrays_26_Code(n,i+1,sum-list[i],list)
if __name__ =='__main__':
    list = []
    n = int(input())
    for _ in range(n):
        list.append(int(input()))
    if(arrays_26_Code(n,0,0,list)):
        print("YES")
    else:
        print("NO")