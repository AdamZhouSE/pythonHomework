
def find(num):
    while True:
        temp=0
        for item in str(num):
            temp+=(int(item)*int(item))
        if record.count(temp)!=0:
            return False
        else:
            if temp==1:
                return True
            record.append(temp)
            num=temp

if __name__ == '__main__':
    num = int(input())
    record = []
    print(find(num))