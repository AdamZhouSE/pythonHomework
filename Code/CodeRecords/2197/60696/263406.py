class Person:
    def __init__(self, num, next=0):
        self.num = num
        self.next = next


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        num = int(input())
        if num == 1:
            print(num)
            continue
        head = Person(1)
        head.next = Person(2)
        p = head.next
        for j in range(2, num+1):
            if j == num:
                p.next = head
            else:
                p.next = Person(j+1)
            p = p.next
        p = head
        for j in range(1, num):
            p.next = p.next.next
            p = p.next
        print(p.num)