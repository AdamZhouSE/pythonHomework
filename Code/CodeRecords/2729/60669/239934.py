list=eval(input())

left=0
right=len(list)-1

result=0

while (left<=right):
    mid=int((left+right)/2)    # 根据题目他必是整数
    if list[mid]==list[mid+1]:
        if (mid%2==0):    # 如果此时他的index是偶数 说明左侧一共是偶数个数 因此左侧是没有单数个元素的 下面同理
            left=mid+2
        else:
            right=mid-1
    elif list[mid]==list[mid-1]:
        if (mid%2==0):
            right=mid-2
        else:
            left=mid+1
    else:
        result=list[mid]
        break

print(result)