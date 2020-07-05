

if __name__ == '__main__':
    candies = int(input())
    num_people = int(input())
    re = [0 for i in range(num_people)]
    p = 1
    i = 0
    while candies>0:

        if p<=candies:
            re[i] += p
            p+=1
        else:
            re[i] != candies
            break
        i +=1
        if i == num_people:
            i=0